#!/bin/bash  
yum update -y  
yum install -y httpd  
systemctl start httpd  
systemctl enable httpd  
cd /var/www/html  
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
