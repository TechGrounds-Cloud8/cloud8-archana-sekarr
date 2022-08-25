# Decision Documentation 
## Region

Based on the project requirements, having one region is sufficient because the vpcs demand isolation and that can be done in one region itself for now. IF the goal is security and if the client wants to have a highly available architecture, then we can move this to another region if needed in the future.

In this phase of the project, high availability is not part of the requirements, so I have deployed only one instance of application server and management server.

I chose the eu-central-1 region because it is the closest available region to the customer.

## EC2

I chose free tier instances such as t3.nano and t2.micro for this phase of the project. This can be upgraded based on the project's future requirements.

## Storage

S3 encryption at rest is enabled to ensure the user data script is encrypted at rest.

## Backup 

The created vault is also encrypted at rest to ensure data is safe. 

# Decisions made wrt version1.1 are as follows :

## Using the public subnet for the application webserver

The secure way of deploying the application web server involves deploying the ec2 instances in the private subnet and adding a NAT gateway for internet connection to the instances in the private subnet.

But NAT is expensive and it is not preferred by the product owner as a solution. An alternative was explored, where the ec2 instances were deployed in the public subnet but with no public IP atached to them. However, this also didnt give access to the internet to install the necessary packages mentioned in the user data.

## User data for the management server

To automate the installation of the openssh server in the management server, User data is added with the required commands to install, start the server and configure the firewalls.