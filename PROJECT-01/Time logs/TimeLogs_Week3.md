# Time Log - Week 3

## Log 18-07-2022

### Daily Report

Created ec2 instance with windows image; updated the nacls, created a security group on ec2 instance to allow traffic from port 3389.

### Challenges

I faced an error where CDK modules were not properly recognized and this was failing the deployments.

### Solutions

I had to recreate the virtual environment and re-install the project dependencies to overcome the challenge.

### Learnings

 learning process involved in fixing the above issue.


## Log 19-07-2022

### Daily Report

Created nacls for web server and set permissions for ec2 to access the s3 bucket

### Challenges

with 40 degrees outside, it was quite a challenge to remain productive.

### Solutions

Tried to work mostly during the day before the heat kicked in

### Learnings

Never take nature for granted and I also learnt that the permissions for ec2 to access s3 bucket can be set either from the s3 resource policy or from ec2 itself. I found the code for ec2 to access S3 easier.

## Log 20-07-2022

### Daily Report

Understood that we need a back up of the server only in version 1.0 so creating a snapshot of the ebs volume is not required for now.

### Challenges

I found it hard to convince myself to create a back up of the server with basically nothing in it. I was wondering why we need a back up of the root volume where there is no image or any resource now to make a back up. I thought that i should create a snapshot of ebs volume and store it in s3. 

### Solutions

With the help of my teammates, i understood that for this version the back up of the server is only required, as there is only one volume, the data gets stored there and in the future there may be logs so taking a back up of the root volume in this case, is the same as making a backup of the complete server.

### Learnings

I had to think and read a lot to understand why we use AWS back up and discussing with my teammates opens up a lot of avenues.


## Log 21-07-2022


### Daily Report




### Challenges




### Solutions





### Learnings






## Log 22-07-2022


### Daily Report




### Challenges




### Solutions





### Learnings

