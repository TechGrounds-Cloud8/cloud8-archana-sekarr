# Time Log - Week 2

## Log 11-07-2022

### Daily Report

Learnt how to deploy a VPC using CDK. 


### Challenges

Required a lot of strength to process information. then by using the cidr mask of 26, I ended up creating 4 subnets across two AZ’s each with 64 hosts.


### Solutions

Then i realised i need to specify the subnet configuration only once with cidr mask 26 and the cdk will automatically split it across the 2 AZ’s. I also understood while preparing my architecture that one region is sufficient to deploy the vpc's.


### Learnings

Very productive day involving extensive reading and problem-solving. 


## Log 12-07-2022

### Daily Report

Created VPC peering and S3 bucket to store the user data


### Challenges

Again, this involved a lot of reading. I was confused whether to hard code the user data or store it in S3 bucket.


### Solutions


After discussion, I decided to go ahead with S3 bucket because the data needs to be encrypted.

### Learnings

everything mentioned above were part of the learning process.


## Log 13-07-2022

### Daily Report

Creation of web server and management server.


### Challenges

Involved some decisions on which instance type to choose, whether to manually create a key-pair.


### Solutions

Had to refer to couple of videos to understand the creation of the servers,re-read the project requirements thoroughly to make decisions. 

I manually created a key pair in the console and passed that name to the key name while creating the ec2 instance. 

### Learnings

 Most of the times, key pair is generated for one time-action so i created it manually and then gained more knowledge required to create the servers.



## Log 14-07-2022

### Daily Report

Created Security groups and partially working on NACLs, did some knowledge checks


### Challenges

1. I wasnt able to access my webserver after adding NACL and it took a lot of time.
2. Even after adding ephemeral port, when i deployed the ec2 instance, i didnt see the webserver running. After reading, i tried to ssh in to the ec2 instance and when i gave 'curl localhost', i was able to see the server response but it wasnt responding from the console with Public IP 

### Solutions

1. then i learned about Ephemeral port which allows both inbound and outbound traffic.

2. Ben helped me with the server response. I just had to remove s from http and it worked. voila!

### Learnings

The solution mentioned above involed a lot of reading and asking help from  teammates always works best.


## Log 15-07-2022

### Daily Report

More knowledge checks and worked on documentation

### Challenges

not much


### Solutions


update your decision documents as and when you make a decision instead of noting it elsewhere roughly


### Learnings

same as above