# LNX-04 Users and groups
- Learning to create new user, create password and how to create different groups and list them.

## Key terminology
- root user(has complete access to Linux)
- super user == user with root privileges
- sudo - (super user do, allows to run programs with the security privileges of another user, as the superuser)
- useradd -m USERNAME (to add a user)
- passwd USERNAME (to assign password to a user)
- useradd USERNAME –d /home/new (to change home directory for user)
- userdel USERNAME (to remove user)
- groupadd GROUPNAME (to add a group)
- usermod (to make modifications on useraccount)
- usermod -a -G GROUP USER (adding user to a group) (-a helps the user to stay in other groups too)
- su USER (to switch user)
- cat (print) - to read the file and print the content in terminal
- /etc/passwd (a file that contains list of all users with every information)
- /etc/group (information of every group) 


## Exercise

### Sources
- [users and groups tutorial](https://www.youtube.com/watch?v=mofySWmEuL4)
- [users, groups and permissions](https://medium.com/codex/users-groups-and-permissions-in-linux-93895ae57d93)
- [create new user](https://www.w3cschoool.com/linux-create-user)
- [listing users](https://linuxize.com/post/how-to-list-users-in-linux/)
- [listing groups](https://linuxhint.com/list-all-groups-linux/)
- [su command](https://linuxize.com/post/su-command-in-linux/)

### Overcome challanges
This assignment was quite challenging to understand the working of each command and how the groups are created. After referring to many videos and with the inputs from my colleagues, I was able to complete it.

### Results

I followed the following steps to achieve the result.

1. Created user and added password
![LNX-04-01](../../../00_includes/DAY3_LINUX/LNX-04/LNX-04-01.png)

2. Added user to admin group
![LNX-04-02](../../../00_includes/DAY3_LINUX/LNX-04/LNX-04-02.png)

3. Switch user/admin
![LNX-04-03](../../../00_includes/DAY3_LINUX/LNX-04/LNX-04-03.png)

4. Listing user twinkle
![LNX-04-04](../../../00_includes/DAY3_LINUX/LNX-04/LNX-04-04.png)

5. Listing groups with user twinkle
![LNX-04-05](../../../00_includes/DAY3_LINUX/LNX-04/LNX-04-05.png)




