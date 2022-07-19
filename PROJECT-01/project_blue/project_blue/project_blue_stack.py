from operator import ge
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3
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
                             block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                             encryption=s3.BucketEncryption.S3_MANAGED)

        # Creation of Application web server
        application_web_server = ec2.Instance(self, 'application-server-ec2',
                                              instance_name='app-server-ec2',
                                              instance_type=ec2.InstanceType.of(
                                                    ec2.InstanceClass.T3, ec2.InstanceSize.NANO),
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
            # peer= ec2.Peer.ipv4("77.163.188.237/32"),
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="admin home ip to connect see the application webserver",
        )

        #  TODO remove this after testing
        # allowing access to port 22 only from the admin's home ip
        application_web_server_security_group.add_ingress_rule(
            # TODO revert the change to use the admin ip
            peer=ec2.Peer.ipv4("77.163.188.237/32"),
            connection=ec2.Port.tcp(22),
            description="admin home ip to connect see the application webserver",
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
            rule_number=250,
            traffic=ec2.AclTraffic.tcp_port(3389),
            network_acl_entry_name="allowing rdp ingress",
            rule_action=ec2.Action.ALLOW,
            id="management-vpc-id-ingress-win-rdp"
        )
        # creating entry to add egress on all ports to admin home ip for ssh on port 22
        management_network_nacl.add_entry(
            cidr=ec2.AclCidr.ipv4("77.163.188.237/24"),
            direction=ec2.TrafficDirection.EGRESS,
            rule_number=300,
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
            peer=ec2.Peer.ipv4("77.163.188.237/32"),
            connection=ec2.Port.tcp(3389),
            description="admin home ip to connect with the management win server",
        )

        # adding the created security group to the management server ec2
        management_server_windows.add_security_group(management_security_group_win)        