from operator import ge
import os
from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_backup as backup_service,
    aws_events as events,
    aws_s3_deployment as s3_deployment
)


class ProjectBlueStack(Stack):
    # Creating Application VPC and subnets
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        applicationVpc = ec2.Vpc(self, "project-blue-application-vpc", cidr="10.20.20.0/24",
                                 max_azs=2,
                                 nat_gateways=0,
                                 subnet_configuration=[
                                     ec2.SubnetConfiguration(
                                         name='Public-Subent',
                                         subnet_type=ec2.SubnetType.PUBLIC,
                                         cidr_mask=26,
                                     )
                                 ],

                                 )

        # Creating Management VPC and subnets
        managementVpc = ec2.Vpc(self, "project-blue-management-vpc", cidr="10.10.10.0/24",
                                max_azs=2,
                                nat_gateways=0,
                                subnet_configuration=[
                                    ec2.SubnetConfiguration(
                                        name='Public-Subent',
                                        subnet_type=ec2.SubnetType.PUBLIC,
                                        cidr_mask=26,
                                    )
                                ],
                                )

        # Creating VPC Peering between application vpc and management vpc
        vpc_peering = ec2.CfnVPCPeeringConnection(self, "app-vpc-mgmt-vpc-peering",
                                                  peer_vpc_id=managementVpc.vpc_id,
                                                  vpc_id=applicationVpc.vpc_id,
                                                  )

        # creating an S3 bucket to store the user data script
        s3Bucket = s3.Bucket(self, 'admin-server-files',
                             bucket_name="project-blue-server-files",
                             block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                             encryption=s3.BucketEncryption.S3_MANAGED,
                             removal_policy=RemovalPolicy.DESTROY,
                             auto_delete_objects=True)

        uploadScriptsToS3 = s3_deployment.BucketDeployment(self, 's3-bucket-deployment',
                                                           destination_bucket=s3Bucket,
                                                           sources=[s3_deployment.Source.asset(os.path.join(
                                                               os.path.dirname("."), "user_config"))]
                                                           )
        # Creation of Application web server
        application_web_server = ec2.Instance(self, 'application-server-ec2',
                                              instance_name='app-server-ec2',
                                              instance_type=ec2.InstanceType.of(
                                                    ec2.InstanceClass.T3, ec2.InstanceSize.MICRO),
                                              vpc=applicationVpc,
                                              vpc_subnets=ec2.SubnetSelection(
                                                  subnet_type=ec2.SubnetType.PUBLIC,
                                                  # availability_zones=['eu-central-1a']
                                              ),
                                              # link for machine image
                                              # https://bobbyhadz.com/blog/aws-cdk-ec2-instance-example
                                              machine_image=ec2.AmazonLinuxImage(
                                                  generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                                              ),
                                              # Adding a block device and enabling encryption on the ebs volume created by default
                                              block_devices=[
                                                  ec2.BlockDevice(device_name="/dev/xvda",
                                                                  volume=ec2.BlockDeviceVolume.ebs(20, encrypted=True))],
                                              key_name='project-blue-key-pair',
                                              )

        localPath = application_web_server.user_data.add_s3_download_command(
            bucket=s3Bucket,
            bucket_key="userdata_configuration.sh",
            region='eu-central-1'
        )

        application_web_server.user_data.add_execute_file_command(
            file_path=localPath,
        )

        apacheIndexFilePath = application_web_server.user_data.add_s3_download_command(
            bucket=s3Bucket,
            bucket_key="index.html",
            local_file="/tmp/index.html",
            region='eu-central-1')

        # application_web_server.user_data.add_commands("chmod 775 -R /var/www/html")
        application_web_server.user_data.add_commands(
            'mkdir -p "/var/www/html" && cp "/tmp/index.html" "/var/www/html/index.html"')

        s3Bucket.grant_read(application_web_server)

        # Creating a security group to attach with the application server
        application_web_server_security_group = ec2.SecurityGroup(self,
                                                                  'application-server-sg',
                                                                  vpc=applicationVpc,
                                                                  allow_all_outbound=True,
                                                                  security_group_name="application-server-sg",
                                                                  )
        # allowing access to port 80 only from the admin's home ip
        application_web_server_security_group.add_ingress_rule(
            # TODO revert the change to use the admin ip
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="admin home ip to connect see the application webserver",
        )

        # allowing access to port 443 only from the admin's home ip
        application_web_server_security_group.add_ingress_rule(
            # TODO revert the change to use the admin ip
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="admin home ip https to connect see the application webserver",
        )

        #  TODO remove this after testing
        # allowing access to port 22 only from the admin's home ip
        application_web_server_security_group.add_ingress_rule(
            # TODO revert the change to use the admin ip
            peer=ec2.Peer.ipv4("77.163.188.237/32"),
            connection=ec2.Port.tcp(22),
            description="admin home ip to connect see the application webserver",
        )

        # Creating NACL on the application servers subnet to allow traffic over port 80 (TODO for now only from admin's home IP)

        application_network_nacl = ec2.NetworkAcl(self, id='application-nacl',
                                                  vpc=applicationVpc,
                                                  network_acl_name="application-vpc-nacl",
                                                  subnet_selection=ec2.SubnetSelection(
                                                      subnet_type=ec2.SubnetType.PUBLIC
                                                  )
                                                  )

        # creating entry to add ingress on port 80 from the admins home ip
        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),
            direction=ec2.TrafficDirection.INGRESS,
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(80),
            network_acl_entry_name="allowing ingress on port 80",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-id-ingress"
        )

        # creating entry to add egress on all ports to admin home ip from port 80
        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),
            direction=ec2.TrafficDirection.EGRESS,
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(80),
            network_acl_entry_name="allowing egress on port 80",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-id-egress"
        )

        # TODO remove after the ssh access is configured from the management server
        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.ipv4("77.163.188.237/24"),
            direction=ec2.TrafficDirection.INGRESS,
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port(22),
            network_acl_entry_name="allowing rdp ingress",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-ingress-ssh"
        )

        # creating entry to add egress on all ports to admin home ip for ssh on port 22
        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.ipv4("77.163.188.237/24"),
            direction=ec2.TrafficDirection.EGRESS,
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            network_acl_entry_name="allowing ssh egress",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-egress-ssh"
        )

        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),
            direction=ec2.TrafficDirection.INGRESS,
            rule_number=400,
            traffic=ec2.AclTraffic.tcp_port(443),
            network_acl_entry_name="allowing 443 ingress",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-ingress-https"
        )

        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),
            direction=ec2.TrafficDirection.EGRESS,
            rule_number=400,
            traffic=ec2.AclTraffic.tcp_port(443),
            network_acl_entry_name="allowing 443 egress",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-egress-https"
        )

        # adding the created security group to the application server
        application_web_server.add_security_group(
            application_web_server_security_group)

        # Creation of Management server
        management_server = ec2.Instance(self, 'management-server-ec2',
                                         instance_name='mgmt-server-ec2',
                                         instance_type=ec2.InstanceType.of(
                                             ec2.InstanceClass.T3, ec2.InstanceSize.NANO),
                                         vpc=managementVpc,
                                         vpc_subnets=ec2.SubnetSelection(
                                             subnet_type=ec2.SubnetType.PUBLIC,
                                             # availability_zones=['eu-central-1a']
                                         ),
                                         # link for machine image
                                         # https://bobbyhadz.com/blog/aws-cdk-ec2-instance-example
                                         machine_image=ec2.AmazonLinuxImage(
                                             generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                                         ),
                                         key_name='project-blue-key-pair'
                                         )

        # Creating NACL on the management servers subnet to allow traffic over port 22 only from the admin's home ip

        management_network_nacl = ec2.NetworkAcl(self, id='management-nacl',
                                                 vpc=managementVpc,
                                                 network_acl_name="management-vpc-nacl",
                                                 subnet_selection=ec2.SubnetSelection(
                                                     subnet_type=ec2.SubnetType.PUBLIC
                                                 )
                                                 )

        # creating entry to add ingress on port 22 from the admins home ip
        management_network_nacl.add_entry(
            cidr=ec2.AclCidr.ipv4("77.163.188.237/24"),
            direction=ec2.TrafficDirection.INGRESS,
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            network_acl_entry_name="allowing ssh ingress",
            rule_action=ec2.Action.ALLOW,
            id="management-vpc-id-ingress"
        )

        management_network_nacl.add_entry(
            cidr=ec2.AclCidr.ipv4("77.163.188.237/24"),
            direction=ec2.TrafficDirection.INGRESS,
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port(3389),
            network_acl_entry_name="allowing rdp ingress",
            rule_action=ec2.Action.ALLOW,
            id="management-vpc-id-ingress-win-rdp"
        )
        # creating entry to add egress on all ports to admin home ip for ssh on port 22
        management_network_nacl.add_entry(
            cidr=ec2.AclCidr.ipv4("77.163.188.237/24"),
            direction=ec2.TrafficDirection.EGRESS,
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            network_acl_entry_name="allowing ssh and rdp egress",
            rule_action=ec2.Action.ALLOW,
            id="management-vpc-id-egress"
        )

        # Creating a security group to attach with the management server
        management_security_group = ec2.SecurityGroup(self,
                                                      'management-server-sg',
                                                      vpc=managementVpc,
                                                      allow_all_outbound=True,
                                                      security_group_name="management-server-sg",
                                                      )
        # allowing access only from the admin's home ip
        management_security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4("77.163.188.237/32"),
            connection=ec2.Port.tcp(22),
            description="admin home ip to connect with the management server",
        )

        # adding the created security group to the management server ec2
        management_server.add_security_group(management_security_group)

        management_server_windows = ec2.Instance(self, 'management-server-ec2-windows',
                                                 instance_name='mgmt-server-ec2-win',
                                                 instance_type=ec2.InstanceType.of(
                                                     ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
                                                 vpc=managementVpc,
                                                 vpc_subnets=ec2.SubnetSelection(
                                                     subnet_type=ec2.SubnetType.PUBLIC,
                                                     # availability_zones=['eu-central-1a']
                                                 ),
                                                 # link for machine image
                                                 machine_image=ec2.WindowsImage(
                                                     version=ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
                                                 key_name='project-blue-key-pair'
                                                 )
        # Creating a security group to attach with the management server
        management_security_group_win = ec2.SecurityGroup(self,
                                                      'management-server-win-sg',
                                                      vpc=managementVpc,
                                                      allow_all_outbound=True,
                                                      security_group_name="management-server-win-sg",
                                                      )
        # allowing access only from the admin's home ip
        management_security_group_win.add_ingress_rule(
            peer=ec2.Peer.ipv4("77.163.188.237/24"),
            connection=ec2.Port.tcp(3389),
            description="admin home ip to connect with the management win server",
        )

        # adding the created security group to the management server ec2
        management_server_windows.add_security_group(management_security_group_win)

        # TODO ask question on this ?
        # By default a backup vault is created with the BackupPlan when its not mentioned explicity!. So why should be
        # we create one explicity and mention it here ??

        # code to create the backup valut explicitly
        # app_server_backup_vault = backup_service.BackupVault(self, "server_backup_vault",
        # backup_vault_name="app-server-backup-vault")

        # back up plan for the web server - daily back up and retention for 7 days
        backup_plan =  backup_service.BackupPlan(self, "server_backup",
        # TODO uncomment the line below if decided to use the backup valut created above
        # backup_vault= app_server_backup_vault
        )

        # created a custom rule that runs ever day at 8 and takes a backup daily. The retention is set to 7 days
        backup_plan_rule = backup_service.BackupPlanRule(
        delete_after=Duration.days(7),
        schedule_expression=events.Schedule.cron(minute='0', hour= '8'))
        backup_plan.add_rule(backup_plan_rule)

        # Configuring the resource that should be backedup
        backup_plan.add_selection(
        id="backup-selection-id",
        resources=[backup_service.BackupResource.from_ec2_instance(application_web_server)])
