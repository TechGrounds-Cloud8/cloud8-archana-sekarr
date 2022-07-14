# Questions for Product Owner
1. Why are we hosting the app in the public subnet? wouldnt it be better to put it in a private subnet to improve security and limit the accessibility from the internet.

2. what is the availability requirement of the product? I see the web server being deployed in only AZ. since there are 2 AZ, wouldnt it be better to deploy it in both the AZs?

3. What is the reason behind having the Management server in one Region and the app server in another region? Why cant I deploy the Mgmt server and app server within the same region? 

If we deploy both in the same region, cant we just have just one VPC to reduce the operational overhead?

4. you have mentioned usage of VM disks. What are your storage requirements for your app and management server? How big a disk size should we have? (Storage GB size) There are multiple storage types? 

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

Amazon EBS provides the following volume types, which differ in performance characteristics and price, so that you can tailor your storage performance and cost to the needs of your applications. The volumes types fall into these categories:

Solid state drives (SSD) — Optimized for transactional workloads involving frequent read/write operations with small I/O size, where the dominant performance attribute is IOPS.

Hard disk drives (HDD) — Optimized for large streaming workloads where the dominant performance attribute is throughput.

Previous generation — Hard disk drives that can be used for workloads with small datasets where data is accessed infrequently and performance is not of primary importance. We recommend that you consider a current generation volume type instead.

Solid state drives (SSD)
The SSD-backed volumes provided by Amazon EBS fall into these categories:

General Purpose SSD — Provides a balance of price and performance. We recommend these volumes for most workloads.

Provisioned IOPS SSD — Provides high performance for mission-critical, low-latency, or high-throughput workloads..

Q for me -- how to encrypt EBS volumes? KMS?
   




