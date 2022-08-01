# Simple Storage Service (S3)

This exercise helps in understanding S3 better along with the different classes. Also, learnt how to use S3 to host a static website.

Introduction:

AWS offers object based storage in the form of S3. S3 makes use of buckets as a container for objects. A single object in S3 has a maximum size of 5TB. However, the total size of a bucket is virtually unlimited.

In S3, you pay for:
- GBs storage per month
- Transfer OUT to out of the region
- PUT, COPY, POST, LIST, and GET requests
You don’t pay for:
- Transfer IN to Amazon S3
- Transfer OUT from S3 to CloudFront or EC2 in the same region

Besides storing data for all kinds of purposes (big data, storing videos, archiving, etc.), S3 has another use case: hosting static websites.
## Key terminology

-  Object storage - Organizations today face difficulties cost-effectively storing what is an unprecedented amount of data. Much of this data is unstructured and doesn’t fit easily into traditional databases. Email, videos, photos, webpages, audio files, sensor data, and other types of web content are all unstructured, and finding efficient and affordable ways to manage them has become problematic. Cloud object storage is increasingly seen as the solution to this challenge. With AWS object storage solutions, you manage your storage in one place with an easy-to-use application interface. You can use policies to optimize storage costs, tiering between different storage classes automatically. AWS makes storage easier to use to perform analysis, gain insights, and make better decisions faster. 

- Buckets - A bucket is a container for objects stored in Amazon S3. You can store any number of objects in a bucket and can have up to 100 buckets in your account. Every object is contained in a bucket. To upload your data (photos, videos, documents, etc.) to Amazon S3, you must first create an S3 bucket in one of the AWS Regions. In traditional NAS terms, a bucket would be a “folder”, but because S3 deals with objects and not files, the distinction becomes important.

Bucket names must be globally unique. That is, even other AWS accounts in different regions cannot share the same bucket name. Buckets, and objects within buckets, can be accessed using a URL.

- Bucket policy - A bucket policy is a resource-based policy that you can use to grant access permissions to your bucket and the objects in it. Only the bucket owner can associate a policy with a bucket. The permissions attached to the bucket apply to all of the objects in the bucket that are owned by the bucket owner. These permissions do not apply to objects owned by other AWS accounts. The bucket policy acts as an access control list. Data can be encrypted for even further protection.

Different storage classes:

- S3 Standard - S3 Standard offers high durability, availability, and performance object storage for frequently accessed data. Because it delivers low latency and high throughput, S3 Standard is appropriate for a wide variety of use cases, including cloud applications, dynamic websites, content distribution, mobile and gaming applications, and big data analytics. This is the best choice if you access data more than once a month.

- S3 Standard-Infrequent Access(IA) - S3 Standard-IA is for data that is accessed less frequently, but requires rapid access when needed. S3 Standard-IA offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and per GB retrieval charge. This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and as a data store for disaster recovery files. This storage class is ideal for data retained for at least a month and accessed once every month or two.

- S3 One-zone Infrequent Access(IA) - It is for data that is accessed less frequently, but requires rapid access when needed. Unlike other S3 Storage Classes which store data in a minimum of three Availability Zones (AZs), S3 One Zone-IA stores data in a single AZ and costs 20% less than S3 Standard-IA. S3 One Zone-IA is ideal for customers who want a lower-cost option for infrequently accessed data but do not require the availability and resilience of S3 Standard or S3 Standard-IA. It’s a good choice for storing secondary backup copies of on-premises data or easily re-creatable data. You can also use it as cost-effective storage for data that is replicated from another AWS Region using S3 Cross-Region Replication.

- S3 Glazier - The Amazon S3 Glacier storage classes are purpose-built for data archiving, providing you with the highest performance, most retrieval flexibility, and the lowest cost archive storage in the cloud.

There are three archive storage classes optimized for different access patterns and storage duration. 

i) For archive data that needs immediate access, such as medical images, news media assets, or genomics data, choose the **S3 Glacier Instant Retrieval** storage class, an archive storage class that delivers the lowest cost storage with milliseconds retrieval. 

ii) For archive data that does not require immediate access but needs the flexibility to retrieve large sets of data at no cost, such as backup or disaster recovery use cases, choose **S3 Glacier Flexible Retrieval** (formerly S3 Glacier), with retrieval in minutes or free bulk retrievals in 5—12 hours. 

iii) To save even more on long-lived archive storage such as compliance archives and digital media preservation, choose **S3 Glacier Deep Archive**, the lowest cost storage in the cloud with data retrieval within 12 hours. 

All these storage classes provide multi-Availability Zone (AZ) resiliency by redundantly storing data on multiple devices and physically separated AWS Availability Zones in an AWS Region.

- S3 Intelligent-Tiering - The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically moving data to the most cost-effective access tier when access patterns change, without operational overhead or impact on performance. It is more a cost optimization tool than a class on its own.

- Static websites - deliver HTML, JavaScript, images, video and other files to your website visitors. Static websites are very low cost, provide high-levels of reliability, require almost no IT administration, and scale to handle enterprise-level traffic with no additional work.

- S3 PUT, COPY, POST, LIST, and GET requests - These are different APIs in S3 that can be used to store/update/list/retrieve the objects in a bucket.

### Exercise

Requirements:
- Your AWS environment
- A cat picture (jpg or png)
- AWS’ demo website (index.html, script.js, style.css; can be found in the Google Drive)
- A peer

Exercise 1
1. Create new S3 bucket with the following requirements:
Region: Frankfurt (eu-central-1)
2. Upload a cat picture to your bucket.
3. Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.

Exercise 2
1. Create new bucket with the following requirements:
Region: Frankfurt (eu-central-1)
2. Upload the four files that make up AWS’ demo website.
3. Enable static website hosting.
4. Share the bucket website endpoint with a peer. Make sure they are able to see the website.

### Sources

- [Cloud object storage](https://aws.amazon.com/what-is-cloud-object-storage/)
- [Buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)
- [Storage classes - AWS](https://aws.amazon.com/s3/storage-classes/)
- [Create bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)
- [Enable website hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EnableWebsiteHosting.html)
- [Website Access Permission](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html)
### Overcome challanges

This exercise involved a lot of reading to understand how S3 works. Quite an interesting one!

### Results

Exercise 1
1. Create new S3 bucket with the following requirements:
Region: Frankfurt (eu-central-1)

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i1.png)

2. Upload a cat picture to your bucket.

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i2.png)

3. Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.
 
- I understand that whenever I create an object in S3, you get an object URL, which is used to view the object. But when I tried to open that URL after uploading the cat object, I encountered this error as shown in the picture below.

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i3.png)

 I learned that this happened because, when i created the bucket, by default, the public access to the bucket was restricted. If public access is enabled entirely on the bucket, anyone across the world can access it any number of time which will increase your AWS bill as you are also chargeable for transfer of data. 

- By using Pre-signed URL, you can limit the access to an object for a certain duration. So I created a pre-signed URL [my Pre-signed URL](https://archcatalistic.s3.eu-central-1.amazonaws.com/cat_PNG50509.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIBmeGDCX33%2FWFQaZfgbwER0fxx1jx%2F%2FOxLQuiKgF599qAiEAs8NQVElTWmrV2umbafiHVts88AyfYYm%2B075kBKCrBVAq5AIIfBAAGgwxMDUxMjk4NjUyNjIiDKgUs4Y1Msn1KoTYeirBAofCkbYQReWluvEW%2BD5y%2FuUez1hqdvhny1Y3mqVjKXdtbjCOX4FuEIXkMDtS6RW4zBgJhY4DB2%2FClC%2BIW7KuKZHD73xtgveX98ruynOQz%2FDAxBgTgsLepMq31YLELVIfNM%2FLTZmBOeX9ItbSboRQacGzjs1q%2BoOPnAcxH9RkRjKnJk9UloVxQhsXxPcM50%2BL6qBwivFg%2FLtYKfsHqBRf2iF06HyeMta3Zct2OyD2Kv0KfKrdBuMusu%2FkptVCmjYU9fQqUigf%2F6XX3DCT39lhNZ6yMzy71wS6kignLKs2K1K7iJ0gSiJwTAh4PzwfjG1xbiXcA01Stm3tcsIeD5XLARD%2BT%2FmzQS%2BRu7jXSgHZ81epAic46ugWerC3Ud5zm0%2F5ievoF%2BJ1450WsCZ%2BVfcYf1%2BjQgiSCK%2FR326uDgqEIhQC%2BzCJw7SUBjqzApkyK1nduqIg3WR%2F%2Bal2ssu2LDMfWZCOPc5CFjIW%2BTu%2BdUOqd3mMZ%2BPJKyOu%2F%2BSp13OG6hTriTiTc%2FdcMCBrBdjgAwbyZZIceQXMG8N%2BnvZmjCgWx8ktocUv0jGJCQHiza09SYeUQrH5hIsSZ1AHaT79nLTbi2siAmHT%2FjIZaIwi7Q2ZbS8pPHQN4TpdPctrsW06TRzk13hkdWOWuQikqwMQuoRxoYuP1OTaEMyE8xLaaa4qwKgMxpKuSGLcndoonkEkEzxbfHz1EZTSRE4n0eSmdZ2xDQ4KH%2BQOrwNpHRF39dCmSlJDhPkFkghbiEaze%2Fgl3xuyx8odIG9dPJ%2FOSD7GQxk4AR0JvMslR4hEsipLkje%2BBxrFQ%2Bu40sCY5g33k5M1jNYHKoGdllzGP4z3M8%2FLaW0%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220524T183828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIARQ6R2OAXIRD6AWWU%2F20220524%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=bcceec8ad843172cb456759b2336bb9997f5dc50d301c2684abeff3b2e5bd92d) and shared it with my teammates. 

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i4.png)


![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i5.png)

Exercise 2
1. Create new bucket with the following requirements:
Region: Frankfurt (eu-central-1)

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i6.png)

2. Upload the four files that make up AWS’ demo website.

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i7.png)

3. Enable static website hosting.

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i8.png)

- Public access was denied by default during bucket creation. In order to make the website accessible to public, I had to enable public access for the bucket and the objects as shown below.

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i9.png)

- I also had to edit the bucket policy by following the instructions in this [link](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html) as shown below. 

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i10.png)


4. Share the bucket website endpoint with a peer. Make sure they are able to see the website.

After enabling the above configuration, my peers were able to access the website.

![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i11.png)


![AWS-05-SimpleStorageService(S3)](../00_includes/AWS-Week1/AWS-05/i12.png)