# Time Log - Week 5

## Log 01-08-2022

### Daily Report

 Created requirements doc,Jira board and created vpc with private subnets.
### Challenges

 I was confused whether to use private with nat or isolated subnet
### Solutions

Figured out nat costs 0.04cents per hour and it's very expensive. Also, Nat isnt required in this case.

### Learnings

Nat is not required as we can use load balancer to connect to the internet instead.

# Time Log - Week 5

## Log 02-08-2022

### Daily Report

Created ASG and ASG policy
 
### Challenges

I was working with a teammate and we realized that we approached the launch template differently. 
### Solutions

For now, both the methods work so I think it should be fine.
### Learnings

I learnt that the launch template can either be created separately or attach the same from AMI we used for ec2 web server.

# Time Log - Week 5

## Log 03-08-2022

### Daily Report

Created application load balancer, opened listener ports, redirected http to https and target groups
### Challenges

Had some questions regarding attaching of security groups and which ports to enable.

### Solutions

For now, I have configured port 443 under listener. Need to work on certification tomorrow.

### Learnings

I learnt that using a private SSL certificate only signed by the CA is very expensive. Casper suggested that using a free SSL certificate or a self-signed certificate are the best options in this case.

# Time Log - Week 5

## Log 04-08-2022

### Daily Report

Configured the user data and working on self-signed ssl certification
### Challenges

 It was very challenging to read the user data in the console and i came across 502 bad gateway error. 

### Solutions

After the Q&A, i learnt a simpler way to over come the 502 error. When I set up an ec2 instance, I need to override the default settings to one that doesn't have a public IP. By doing this, we can ensure that the web server isn't be publicly accessible.

### Learnings

I need to work on fixing the error tomorrow and I now know how to approach it. 

# Time Log - Week 5

## Log 05-08-2022

### Daily Report

 
### Challenges

 

### Solutions



### Learnings




