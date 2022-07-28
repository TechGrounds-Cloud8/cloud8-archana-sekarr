# Decision Documentation 
## Region

Based on the project requirements, having one region is sufficient because the vpcs demand isolation and that can be done in one region itself for now. IF the goal is security and if the client wants to have a highly available architecture, then we can move this to another region if needed in the future.

In this phase of the project, high availability is not part of the requirements, so I have deployed only one instance of application server and management server.

I chose the eu-central-1 region because it is the closest available region to the customer.

## VPC's



## EC2

I chose free tier instances such as t3.nano and t2.micro for this phase of the project. This can be upgraded based on the project's future requirements.

### Web server



### Management server




## Storage

S3 encryption at rest is enabled to ensure the user data script is encrypted at rest.

## Backup 

The created vault is also encrypted at rest to ensure data is safe. 