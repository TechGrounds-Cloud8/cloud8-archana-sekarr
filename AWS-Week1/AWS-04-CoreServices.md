# Core Services

Understanding the key services offered by AWS in-depth is essential to approach customers as well as this documentation, acts as a guide for me to prepare for the AWS Cloud Practitioner certification.
## Key terminology

All the key concepts are explained in results
### Exercise
Study:

The AWS Certified Cloud Practitioner (CLF-C01) Exam Guide
 
### Sources

- [AWS services](https://docs.aws.amazon.com/index.html)
- [key services offered by AWS](https://www.i2k2.com/blog/5-best-services-offered-amazon-web-services-2018/)

### Overcome challanges

I learnt the key services offered by AWS with this exercise.
### Results

Some of the many key services offered by AWS have been explained below. Apart from these services, we also need to understand cloud concepts like the Well-Architected Framework or the cloud pricing model for the certification.

1. Amazon Elastic Cloud Compute (EC2) : 
 
The Amazon EC2 service comes under the compute domain and it provides services that help to compute workloads. Amazon EC2 web interface is used to reduce the expensive physical servers by creating virtual machines. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster. Also, they help in managing different features of the virtual servers such as security, ports, and storage. Amazon EC2 is highly preferable while creating a virtual server within a few minutes with just a few clicks according to the user’s operating system conveniently. It offers resizable compute capacity in the cloud. Amazon EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic. This helps a lot to focus more on the project rather than the server maintenance. 

Features of Amazon EC2:

- Virtual computing environments, known as instances

- Preconfigured templates for your instances, known as Amazon Machine Images (AMIs), that package the bits you need for your server (including the operating system and additional software)

- Various configurations of CPU, memory, storage, and networking capacity for your instances, known as instance types

- Secure login information for your instances using key pairs (AWS stores the public key, and you store the private key in a secure place)

- Storage volumes for temporary data that's deleted when you stop, hibernate, or terminate your instance, known as instance store volumes

- Persistent storage volumes for your data using Amazon Elastic Block Store (Amazon EBS), known as Amazon EBS volumes

- Multiple physical locations for your resources, such as instances and Amazon EBS volumes, known as Regions and Availability Zones

- A firewall that enables you to specify the protocols, ports, and source IP ranges that can reach your instances using security groups

- Static IPv4 addresses for dynamic cloud computing, known as Elastic IP addresses

- Metadata, known as tags, that you can create and assign to your Amazon EC2 resources

- Virtual networks you can create that are logically isolated from the rest of the AWS Cloud, and that you can optionally connect to your own network, known as virtual private clouds (VPCs)

2. AWS Lambda - AWS Lambda is a serverless computing platform that runs your code in response to events and automatically manages the underlying compute resources for you. These events may include changes in state or an update, such as a user placing an item in a shopping cart on an ecommerce website.  AWS Lambda automatically runs code in response to multiple events, such as HTTP requests via Amazon API Gateway, modifications to objects in Amazon Simple Storage Service (Amazon S3) buckets, table updates in Amazon DynamoDB, and state transitions in AWS Step Functions. Therefore you don’t need to worry about which AWS resources to launch, or how will you manage them.Instead, you need to put the code on Lambda, and it runs. AWS Lambda function helps you to focus on your core product and business logic instead of managing operating system (OS) access control, OS patching, right-sizing, provisioning, scaling, etc.

3. AWS Elastic Beanstalk - AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time.

There is no additional charge for Elastic Beanstalk - you pay only for the AWS resources needed to store and run your applications.

4. Amazon VPC - Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. It gives you full control over your virtual networking environment, including resource placement, connectivity, and security.This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS. 

There's no additional charge for using a VPC. There are charges for some VPC components, such as NAT gateways, Reachability Analyzer, and traffic mirroring.

5. Amazon Route 53 - It is a highly available and scalable Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost effective way to route end users to Internet applications by translating names like www.example.com into the numeric IP addresses like 192.0.2.1 that computers use to connect to each other. Amazon Route 53 is fully compliant with IPv6 as well. You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.

6. Amazon Simple Storage Service (Amazon S3) - Amazon S3, in simple words is an object storage built to retrieve any amount of data from anywhere. It is an object storage service offering industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.

On creating an account with AWS, it offers 5 GB of S3 standard storage for 12 months with the AWS Free Tier.

7. Amazon S3 Glacier - Amazon S3 Glacier is a secure, durable, and extremely low-cost Amazon S3 storage class for data archiving and long-term backup.
With S3 Glacier, customers can store their data cost effectively for months, years, or even decades. S3 Glacier enables customers to offload the administrative burdens of operating and scaling storage to AWS, so they don't have to worry about capacity planning, hardware provisioning, data replication, hardware failure detection and recovery, or time-consuming hardware migrations. 

8. Amazon CloudFront - Amazon CloudFront is a content delivery network (CDN) service built for high performance, security, and developer convenience. It is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

9. Amazon Relational Database Service (RDS) - It is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud. RDS provides six familiar database engines to choose from, including Amazon Aurora, MySQL, MariaDB, Oracle, Microsoft SQL Server, and PostgreSQL. This means that the code, applications, and tools you already use today with your existing databases can be used with Amazon RDS. Amazon RDS handles routine database tasks such as provisioning, patching, backup, recovery, failure detection, and repair.

Amazon RDS makes it easy to use replication to enhance availability and reliability for production workloads.

10. Amazon DynamoDB - Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. DynamoDB also offers encryption at rest, which eliminates the operational burden and complexity involved in protecting sensitive data. 

11. Amazon CloudWatch - Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), IT managers, and product owners. CloudWatch provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, and optimize resource utilization. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events. You get a unified view of operational health and gain complete visibility of your AWS resources, applications, and services running on AWS and on-premises. You can use CloudWatch to detect anomalous behavior in your environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep your applications running smoothly.

12. Amazon CloudFormation - AWS CloudFormation is a service that helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and CloudFormation takes care of provisioning and configuring those resources for you. You don't need to individually create and configure AWS resources and figure out what's dependent on what; CloudFormation handles that.

13. AWS Identity and Access Management - AWS Identity and Access Management (IAM) provides fine-grained access control across all of AWS. With IAM, you can specify who can access which services and resources, and under which conditions. With IAM policies, you manage permissions to your workforce and systems to ensure least-privilege permissions.

IAM is an AWS service that is offered at no additional charge.

