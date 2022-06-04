# Elastic Beanstalk

Developing an application and managing is an expensive and time-consuming process. AWS offers Beanstalk to manage this process. 

AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.

In simple terms, this platform as a service (PaaS - because it eliminates the management of instracture) takes your application code and deploys it while provisioning the supporting architecture and compute resources required for your code to run. 

You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time.

There is no additional charge for Elastic Beanstalk to deply your applications, you pay only for the AWS resources needed to store and run your applications.


To summarise, the significant features of Elastic Beanstalk are:

1. Elastic Beanstalk is possibly the simplest and fastest way to deploy web applications on AWS.

2. It allows developers to focus on writing code instead of provisioning and configuring AWS resources.

3. Elastic beanstalk handles the auto scaling of resources needed to support your deployed application as demand grows or shrinks.

## Key terminology

- Refer to summary above
### Exercise

Study : Elastic Beanstalk

### Sources

- [Elastic Beanstalk aws documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [Elastic Beanstalk AWS](https://aws.amazon.com/elasticbeanstalk/?sc_channel=EL&sc_campaign=Anim_Explainer_2020_vid&sc_medium=YouTube&sc_content=Video7757&sc_detail=COMPUTE&sc_country=US)
- [Elastic Beanstalk](https://www.hava.io/blog/what-is-aws-elastic-beanstalk)
- [FAQ](https://aws.amazon.com/elasticbeanstalk/faqs/)
- [YT Elastic Beanstalk](https://www.youtube.com/watch?v=uiM1xzOX8Qg)

### Overcome challanges

 I understood the concept by referring to the sources shared above.

### Results
 
Elastic Beanstalk in association with EC2:

When Elastic Beanstalk analyses your application and selects the resources that will be required. **When you deploy an application, Beanstalk will offer an EC2 instance**. It will also allow you to step in and select alternative resources that may be better suited to anticipated use cases it may not know about. For example you could select a higher spec EC2 instance type that better suits your needs. Elastic Beanstalk in association with S3:

Additionally, **AWS Elastic Beanstalk stores application files and, optionally, server log files in Amazon S3**. If you are using the AWS Management Console, the AWS Toolkit for Visual Studio, or AWS Toolkit for Eclipse, an Amazon S3 bucket will be created in your account for you and the files you upload will be automatically copied from your local client to Amazon S3 

This way, Elastic Beanstalk helps in combining the right AWS resources. 

Alternatives and Market Competitors:

Some of the AWS Beanstalk Alternatives & Competitors are Google App Engine, Salesforce Heroku, Azure Web Apps, and Azure App Service. However, the distinguised feature of Beanstalk is that, developers retain full control over the AWS resources powering their application. If developers decide they want to manage some (or all) of the elements of their infrastructure, they can do so seamlessly by using Elastic Beanstalk’s management capabilities.