# Virtual Private Cloud (VPC)

This lesson guides through the design choices around VPC design and IP planning.

Introduction:

Amazon VPC is typically described as a virtual private data center in the cloud. It is a virtual network that is logically isolated from other VPCs.
With a VPC you have full control over the design of the network. You can create subnets, internet gateways (igw), NAT gateways, VPN connections, and more.

There is always a default VPC when you create a new AWS account, but you can add up to 5 non-default VPCs per region per account. This is a soft limit. That is, you can request the limit to be raised.
Many services, like EC2, RDS and ECS require a VPC to be placed into.



## Key terminology

- 


### Exercise


### Sources

- Previous exercises
- [Network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [VPC flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [NACL vs Security group](https://www.javatpoint.com/aws-nacl-vs-security-group)

### Overcome challanges



### Results

![AWS-10-VPC](../00_includes/AWS-Week2/AWS-10/i1.png)