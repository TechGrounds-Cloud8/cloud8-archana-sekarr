# Elastic Container Service (ECS)

In this assignment, We will learn about ECS, a service developed by AWS in response to the rise in popularity of containerization in Cloud. We will also discuss about it's features, pricing, associated services and market competitors. 

## Key terminology

- Containers - A container is a standard unit of software for deploying and managing software in the cloud. Containers are used to abstract applications from the physical environment in which they are running. A container packages all dependencies related to a software component, and runs them in an isolated environment. With containers, commonly running the Docker container engine, applications deploy consistently in any environment, whether a public cloud, a private cloud, or a bare metal machine. Containerized applications are easier to migrate to the cloud. Containers also make it easier to leverage the extensive automation capabilities of the cloud—they can easily be deployed, cloned or modified using APIs provided by the container engine or orchestrator. 

- Docker - Docker is a configuration management tool that is used to automate the deployment of software in lightweight containers. These containers help applications to work efficiently in different environments.

- Docker Image - It is a read-only file with a bunch of instructions. When these instructions are executed, it creates a Docker container. Docker can build images automatically by reading the instructions from a Dockerfile.

- Dockerfile - Dockerfile is a simple text file that consists of instructions to build Docker images. 

- task definition - A task definition is required to run Docker containers in Amazon ECS. A Task Definition is a collection of 1 or more container configurations. Some Tasks may need only one container, while other Tasks may need 2 or more potentially linked containers running concurrently. The Task definition allows you to specify certain parametres for your application such as which Docker image to use, which ports to expose, how much CPU and memory to allot, how to collect logs, and define environment variables.

- task - A Task is created when you run a Task directly, which launches container(s) (defined in the task definition) until they are stopped or exit on their own, at which point they are not replaced automatically. Running Tasks directly is ideal for short-running jobs, perhaps as an example of things that were accomplished via CRON.

- Service - A Service is used to guarantee that you always have some number of Tasks running at all times. If a Task's container exits due to an error, or the underlying EC2 instance fails and is replaced, the ECS Service will replace the failed Task. This is why we create Clusters so that the Service has plenty of resources in terms of CPU, Memory and Network ports to use. To us it doesn't really matter which instance Tasks run on so long as they run. A Service configuration references a Task definition. A Service is responsible for creating Tasks. Services are typically used for long-running applications like web servers.

- ECS on AWS Fargate - AWS Fargate is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. It helps in managing the infrastructure for AWS. With Fargate, the concept of server provisioning, cluster management, and orchestration completely goes away. Amazon ECS uses containers provisioned by Fargate to automatically scale, load balance, and manage scheduling of your containers for availability, providing an easier way to build and operate containerized applications.

- ECS clusters - An Amazon ECS cluster is a logical grouping of tasks or services. Your tasks and services are run on infrastructure that is registered to a cluster. The infrastructure capacity can be provided by AWS Fargate, which is serverless infrastructure that AWS manages, Amazon EC2 instances that you manage, or an on-premise server or virtual machine (VM) that you manage remotely. In most cases, Amazon ECS capacity providers can be used to manage the infrastructure the tasks in your clusters use. When you first use Amazon ECS, a default cluster is created for you, but you can create multiple clusters in an account to keep your resources separate.

### Exercise

Study : ECS

### Sources

- [ECS AWS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [ECS](https://www.techtarget.com/searchaws/definition/Amazon-EC2-Container-Service)
- [FAQ](https://aws.amazon.com/ecs/faqs/)
- [Docker](https://www.simplilearn.com/tutorials/docker-tutorial/what-is-dockerfile)
- [task definition](https://stackoverflow.com/questions/42960678/what-is-the-difference-between-a-task-and-a-service-in-aws-ecs)
- [Containers VS Virtual machines](https://www.eginnovations.com/blog/containers-vs-vms/)
- [Alternatives](https://www.g2.com/products/amazon-elastic-container-service-amazon-ecs/competitors/alternatives)

### Overcome challanges

 I understood the concept by referring to the sources shared above.

### Results
 
## Introduction:

Amazon Elastic Container Service (Amazon ECS) is a highly scalable and fast container management service. ECS manages containers and allows developers to run applications in the cloud without having to configure an environment for the code to run in. It enables developers with AWS accounts to deploy and manage scalable applications that run on groups of servers -- called clusters -- through application program interface (API) calls and task definitions. ECS eliminates the need to install, operate, and scale your own cluster management infrastructure. With simple API calls, you can launch and stop container-enabled applications, query the complete state of your cluster, and access many familiar features like security groups, Elastic Load Balancing, Amazon Elastic Block Store (EBS) volumes, and Identity Access Management (IAM) roles. Amazon ECS enables developers to easily use Docker containers for a range of activities; from hosting a simple website to running complex, distributed microservices that require thousands of containers. ECS evaluates and monitors CPU and memory output to determine the optimal deployment for a container. 

With Amazon ECS, your containers are defined in a task definition that you use to run an individual task or task within a service. In this context, a service is a configuration that you can use to run and maintain a specified number of tasks simultaneously in a cluster. You can run your tasks and services on a serverless infrastructure that's managed by AWS Fargate. Alternatively, for more control over your infrastructure, you can run your tasks and services on a cluster of Amazon EC2 instances that you manage.

## ECS features:

Amazon Elastic Container Service (Amazon ECS) allows you to easily deploy containerized workloads on AWS. The powerful simplicity of Amazon ECS enables you to grow from a single Docker container to managing your entire enterprise application portfolio. Run and scale your container workloads across availability zones, in the cloud, and on-premises, without the complexity of managing a control plane or nodes.

1. Serverless by default with AWS Fargate: 
AWS Fargate is built into Amazon ECS, which means you no longer have to worry about managing servers, handling capacity planning, or figuring out how to isolate container workloads for security. Just define your application’s requirements, select Fargate as your launch type in the console or Command Line Interface (CLI), and Fargate takes care of all the scaling and infrastructure management required to run your containers.

2. Amazon ECS Anywhere: 
With ECS Anywhere, you can use the same familiar Amazon ECS console and operator tools to manage your on-premises container workloads for a consistent experience across your container-based applications. The AWS Systems Manager (SSM) integration automatically and securely establishes trust between your on-premises hardware and the AWS control plane.

3. Security and isolation by design: 
Amazon ECS natively integrates with the Security, Identity, and Management and Governance tools you already trust, which helps you get to production quickly and successfully. You can assign granular permissions for each of your containers, giving you a high level of isolation when building your applications. Launch your containers with the security and compliance levels you have come to expect from AWS.

4. Autonomous control plane operations: 
Amazon ECS is a fully-managed container orchestration service, with AWS configuration and operational best practices built-in, and no control plane, nodes, or add-ons for you to manage. It natively integrates with both AWS and third-party tools to make it easier for teams to focus on building the applications, not the environment.

## Pricing 

There is no additional charge for Amazon ECS. You pay for AWS resources (e.g. Amazon EC2 instances or EBS volumes) you create to store and run your application. You only pay for what you use, as you use it; there are no minimum fees and no upfront commitments.

## How is ECS different from Elastic Beanstalk?

AWS Elastic Beanstalk is an application management platform that helps customers easily deploy and scale web applications and services. It keeps the building block provisioning (e.g., EC2, Amazon RDS, Elastic Load Balancing, AWS Auto Scaling, and Amazon CloudWatch), application deployment, and health monitoring abstracted from the user so they can focus on writing code. You simply specify which container images to  deploy, the CPU and memory requirements, the port mappings, and the container links.

Elastic Beanstalk will automatically handle all the details such as provisioning an Amazon ECS cluster, balancing load, auto-scaling, monitoring, and container placement across your cluster. Elastic Beanstalk is ideal if you want to leverage the benefits of containers withthe simplicity of deploying applications from development to production by uploading a container image. You can work with Amazon ECS directly if you want more fine-grained control for custom application architectures.

Some of the alternatives/market competitors of ECS that offer container management software services are Mirantis Kubernetes Engine (formerly Docker Enterprise), Google Kubernetes Engine (GKE), Red Hat OpenShift Container Platform, and Azure Kubernetes Service (AKS).