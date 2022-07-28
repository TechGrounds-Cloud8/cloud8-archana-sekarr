# Design Documentation

For version 1.0, the entire project is created using CDK and versioned with GIT. So the infrastruture is now available as code. 

AWS services used for this project based on the requirements:

- A VPC
- 2 EC2 instances : 1 each for the management(admin) and appln server 
- S3 for storage of the user data. The user data contains the script to install the apache when the ec2 instance boots up.
- AWS Backup for making daily backups. Back up retained up to 7 days. 
- Security groups and NACLs are made in such a way that the application server can be reached via the managemnt server only.
## VPC's

- 2 vpcs are created. An application VPC with CIDR 10.20.20.0/24 and a management VPC with CIDR 10.10.10.0/24 within the same region. 
- 2 public subnets are created per vpc. 
- VPC peering connection is created between the 2 vpcs. 
- The route tables of each vpc is configured to have the routing information of the other VPC.

## EC2

- We have one EC2 instance running linux OS with an encrypted EBS Volume hosting the application web server.
- Second EC2 instance running the Windows OS with an encrypted EBS Volume and which is the management/admin server. 
- The managament server plays the role of a bastion host/proxy server to reach the resources in the application server.

## Security groups and NACLs.

- Security groups and NACLs are configured such that the web server is reachable from the internet. 
- The management server is reachable from the admin's home IP and the application server is reachable on port 22 from the management server.

## Storage

- S3 bucket is created to store the userdata script. The apache web server index.html file is also stored in S3.
- EBS volumes are created and attached to the EC2 instances and are also encrypted.

## Backup 

- Used the AWS back up service to create the backup plan for 7 days on the application server. 
- The back up is scheduled to be created at 08.00 CET everyday and a vault is created to store the backups. 
- The vault uses the default KMS key to encrypt the backups.

