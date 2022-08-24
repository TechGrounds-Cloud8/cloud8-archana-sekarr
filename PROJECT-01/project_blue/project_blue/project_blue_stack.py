from operator import ge
import os
from re import sub
from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_backup as backup_service,
    aws_events as events,
    aws_s3_deployment as s3_deployment,
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as loadbalancer
)


class ProjectBlueStack(Stack):
    # Creating Application VPC and subnets
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ----------------------------- VPC for application and management server -----------------------------
        applicationVpc = ec2.Vpc(self, "project-blue-application-vpc", cidr="10.20.20.0/24",
            max_azs=3,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public-Subnet',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26,
                ),
            
            ec2.SubnetConfiguration(
                    name='Private-Subnet',
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=26,
                )
            ]        
        )
        
        applicationLoadBalancer = loadbalancer.ApplicationLoadBalancer(self, "app-server-lb", 
            vpc=applicationVpc,
            internet_facing=True
        )
         
        # Redirecting HTTP to HTTPS
        #self.applicationLoadBalancer.add_redirect()
        selfSignedCertificateArn = "arn:aws:acm:eu-central-1:105129865262:certificate/94947276-4270-46f5-88a6-8b8b9e5e6026";
        listener = applicationLoadBalancer.add_listener("app-server-listener", 
            port=443, 
            open=True,
            certificates=[loadbalancer.ListenerCertificate.from_arn(selfSignedCertificateArn)], 
            ssl_policy=loadbalancer.SslPolicy.FORWARD_SECRECY_TLS12
        )
        
        # # ----------------------------- SG for application web server -----------------------------

        # # Creating a security group to attach with the application server
        application_web_server_security_group = ec2.SecurityGroup(self,
            'application-server-sg',
            vpc=applicationVpc,
            allow_all_outbound=True,
            security_group_name="application-server-sg",
        )
        # allowing access to port 80 only from the admin's home ip
        application_web_server_security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="admin home ip to connect see the application webserver",
        )

        # allowing access to port 443 only from the admin's home ip
        application_web_server_security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="admin home ip https to connect see the application webserver",
        )

        # allowing access to port 22 only from the admin's home ip
        application_web_server_security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="admin home ip to connect see the application webserver",
        )

        # # ----------------------------- NACL for application web server -----------------------------

        # Creating NACL on the application servers subnet to allow traffic over port 80 (TODO for now only from admin's home IP)

        application_network_nacl = ec2.NetworkAcl(self, id='application-nacl',
            vpc=applicationVpc,
            network_acl_name="application-vpc-nacl",
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
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

        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),
            direction=ec2.TrafficDirection.EGRESS,
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(80),
            network_acl_entry_name="allowing egress on port 80",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-id-egress"
        )

        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),    
            direction=ec2.TrafficDirection.INGRESS,
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port(443),
            network_acl_entry_name="allowing 443 ingress",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-ingress-https"
        )

        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),    
            direction=ec2.TrafficDirection.EGRESS,
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port(443),
            network_acl_entry_name="allowing 443 egress",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-egress-https"
        )

        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),
            direction=ec2.TrafficDirection.INGRESS,
            rule_number=400,
            traffic=ec2.AclTraffic.tcp_port(22),
            network_acl_entry_name="allowing ssh ingress from anyip",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-ingress-ssh"
        )


        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),
            direction=ec2.TrafficDirection.INGRESS,
            rule_number=500,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            network_acl_entry_name="allowing ephemeral ports ingress from anyip",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-egress-ephemeral ports"
        )

        # opening up the nacl on the app server to allow all outbound traffic to allow yum updates to happen when the user data script runs
        application_network_nacl.add_entry(
            cidr=ec2.AclCidr.any_ipv4(),
            direction=ec2.TrafficDirection.EGRESS,
            rule_number=400,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            network_acl_entry_name="allowing egress on all ports",
            rule_action=ec2.Action.ALLOW,
            id="application-vpc-egress-ssh"
        )

        blockDevice = autoscaling.BlockDevice(device_name="/dev/xvda",
                                volume=autoscaling.BlockDeviceVolume.ebs(20, encrypted=True));

        autoscalingGroup = autoscaling.AutoScalingGroup(self, "ASG",
            vpc=applicationVpc,
            max_capacity=3,
            min_capacity=1,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.NANO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
              vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC   
            ),
            key_name='project-blue-key-pair', 
            security_group= application_web_server_security_group,
            block_devices=[blockDevice],
            associate_public_ip_address = False       
        )

        # Adding the ASG as target to the load balancer listener
        listener.add_targets("target",
            port=80,
            health_check=loadbalancer.HealthCheck(
                enabled=True,
                port="80",
            ),
            targets=[autoscalingGroup],
        )

        # autoscalingGroup.scale_on_request_count("limit-request-per-minute",
        #     target_requests_per_minute=700 
        # )

        # Auto-scaling policy
        autoscalingGroup.scale_on_cpu_utilization(
                'CPU-utlisation-tracking',
                target_utilization_percent=85,
        )

        # Creating Management VPC and subnets
        managementVpc = ec2.Vpc(self, "project-blue-management-vpc", cidr="10.10.10.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public-Subnet',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26,
                )
            ],
            )   

        # ----------------------------- VPC Peering for application and management server -----------------------------
        # Creating VPC Peering between application vpc and management vpc
        vpc_peering = ec2.CfnVPCPeeringConnection(self, "app-vpc-mgmt-vpc-peering",
            peer_vpc_id=managementVpc.vpc_id,
            vpc_id=applicationVpc.vpc_id,
            )

        #  route for application server subnets => management server subnets
        # adding route table entries for application server routetables to have a route for the management server vpc
        for applicationPublicSubnet in applicationVpc.public_subnets:
            ec2.CfnRoute(self, id=f"{applicationPublicSubnet.node.id} peer route",
                destination_cidr_block=managementVpc.vpc_cidr_block,
                route_table_id=applicationPublicSubnet.route_table.route_table_id,
                vpc_peering_connection_id=vpc_peering.ref,
                )

        for applicationPublicSubnet in applicationVpc.isolated_subnets:
            ec2.CfnRoute(self, id=f"{applicationPublicSubnet.node.id} peer route",
                destination_cidr_block=managementVpc.vpc_cidr_block,
                route_table_id=applicationPublicSubnet.route_table.route_table_id,
                vpc_peering_connection_id=vpc_peering.ref,
                )


        # route for management server subnets => application server subnets
        # adding route table entries for management server routetables to have a route for the application server vpc
        for managementPublicSubnet in managementVpc.public_subnets:
            ec2.CfnRoute(self, id=f"{managementPublicSubnet.node.id} route",
                destination_cidr_block=applicationVpc.vpc_cidr_block,
                route_table_id=managementPublicSubnet.route_table.route_table_id,
                vpc_peering_connection_id=vpc_peering.ref,
                )

        # # ----------------------------- S3 bucket for application server user data -----------------------------

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

         # # ----------------------------- User data for application web server -----------------------------
        # # User data for the application web server
        # # download the stored config data from s3
        localPath = autoscalingGroup.user_data.add_s3_download_command(
            bucket=s3Bucket,
            bucket_key="userdata_configuration.sh",
            region='eu-central-1'
        )

        # execute the script to install the apache server
        autoscalingGroup.user_data.add_execute_file_command(
            file_path=localPath,
        )

        #  dowload the index file for the appache server from s3
        apacheIndexFilePath = autoscalingGroup.user_data.add_s3_download_command(
            bucket=s3Bucket,
            bucket_key="index.html",
            local_file="/tmp/index.html",
            region='eu-central-1')

        autoscalingGroup.user_data.add_commands(
            'mkdir -p "/var/www/html" && cp "/tmp/index.html" "/var/www/html/index.html"')

        s3Bucket.grant_read(autoscalingGroup)


        # # ----------------------------- NACL for managment server -----------------------------
        # # Creating NACL on the management servers subnet to allow traffic over port 22 only from the admin's home ip

        # management_network_nacl = ec2.NetworkAcl(self, id='management-nacl',
        #     vpc=managementVpc,
        #     network_acl_name="management-vpc-nacl",
        #     subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        #     )

        # # # creating entry to add ingress on port 22 from the admins home ip
        # management_network_nacl.add_entry(
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     direction=ec2.TrafficDirection.INGRESS,
        #     rule_number=200,
        #     traffic=ec2.AclTraffic.tcp_port(22),
        #     network_acl_entry_name="allowing ssh ingress",
        #     rule_action=ec2.Action.ALLOW,
        #     id="management-vpc-id-ingress-ssh"
        # )

        # management_network_nacl.add_entry(
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     direction=ec2.TrafficDirection.INGRESS,
        #     rule_number=400,
        #     traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
        #     network_acl_entry_name="allowing ssh traffic back from the app server",
        #     rule_action=ec2.Action.ALLOW,
        #     id="management-vpc-id-ingress-ephemeral"
        # )

        # management_network_nacl.add_entry(
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     direction=ec2.TrafficDirection.INGRESS,
        #     rule_number=300,
        #     traffic=ec2.AclTraffic.tcp_port(3389),
        #     network_acl_entry_name="allowing rdp ingress",
        #     rule_action=ec2.Action.ALLOW,
        #     id="management-vpc-id-ingress-win-rdp"
        # )

        # # creating entry to add egress on all ports to admin home ip for ssh on port 22
        # management_network_nacl.add_entry(
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     direction=ec2.TrafficDirection.EGRESS,
        #     rule_number=200,
        #     traffic=ec2.AclTraffic.all_traffic(),
        #     network_acl_entry_name="allowing ssh and rdp egress",
        #     rule_action=ec2.Action.ALLOW,
        #     id="management-vpc-id-egress"
        # )

        # ----------------------------- Ec2 for managment win server -----------------------------

        management_server_windows = ec2.Instance(self, 'management-server-ec2-windows',
            instance_name='mgmt-server-ec2-win',
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
            vpc=managementVpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC,
                
            ),
            # link for machine image
            machine_image=ec2.WindowsImage(
                version=ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
            key_name='project-blue-key-pair',
            block_devices=[
            ec2.BlockDevice(device_name="/dev/xvda",
                            volume=ec2.BlockDeviceVolume.ebs(10, encrypted=True))],
            )

        management_server_windows.user_data.for_windows()
        management_server_windows.add_user_data(
            "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0",
            "Start-Service sshd",
            "Set-Service -Name sshd -StartupType 'Automatic'",
            "New-NetFirewallRule -Name sshd -DisplayName 'Allow SSH' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22",
        )

        # # ----------------------------- SG for managment win server -----------------------------

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

        # allowing access only from the admin's home ip over port 22
        # With port 22 open we can use the windows as a bastion host to jump into the app server instance
        management_security_group_win.add_ingress_rule(
            peer=ec2.Peer.ipv4("77.163.188.237/24"),
            connection=ec2.Port.tcp(22),
            description="admin home ip to connect with the management server over ssh",
        )

        # adding the created security group to the management server ec2
        management_server_windows.add_security_group(
            management_security_group_win)


        # # ---------------------------------- adding a vault explicitly --------------------------------------------
        # # code to create the backup valut explicitly
        # app_server_backup_vault = backup_service.BackupVault(
        #     self, "server_backup_vault",
        #     backup_vault_name="app-server-backup-vault"
        # )

        # # back up plan for the web server - daily back up and retention for 7 days
        # backup_plan = backup_service.BackupPlan(
        #     self, "server_backup",
        #     backup_vault= app_server_backup_vault
        # )

        
        # # created a custom rule that runs ever day at 8 and takes a backup daily. The retention is set to 7 days
        # backup_plan_rule = backup_service.BackupPlanRule(
        #     delete_after=Duration.days(7),
        #     schedule_expression=events.Schedule.cron(minute='0', hour='8'))
        # backup_plan.add_rule(backup_plan_rule)


        # # Configuring the resource that should be backedup
        # backup_plan.add_selection(
        #     id="backup-selection-id",
        #     resources=[ 
        #         backup_service.BackupResource.from_ec2_instance(
        #             application_web_server)]
        # )
