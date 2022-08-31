Using the windows instance as the bastion host to connect to the application server

step 1: Enable the OpenSSH server and the clients by following the instructions in -the blog

https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse

step 2: Test the ssh access to the windows server

 ssh Administrator@ec2-3-70-223-42.eu-central-1.compute.amazonaws.com

step 3: Using the ssh proxy command to jump into the application server

 ssh -i "project-blue-key-pair.pem" -J Administrator@ec2-3-120-176-199.eu-central-1.compute.amazonaws.com ec2-user@10.20.20.125