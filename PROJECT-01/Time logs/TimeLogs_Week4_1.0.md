# Time Log - Week 4

## Log 25-07-2022

### Daily Report

Installed open ssh client and open ssh server on the windows instance. 
### Challenges

Initially i was trying to log into the web server using putty client which was quite a task. 

### Solutions


With the help of my teammates I learnt that i can use the ssh proxy command to connect to the web server via the admin server. Then i started to install ssh server and ssh client on the windows instance. After that i was able to ssh into the application server in a simple way instead of using RDP. In Addition, i had to add the necessary rules in nacl to enable port 22.

### Learnings

As i mentioned above, I took a lot of time to figure out this.