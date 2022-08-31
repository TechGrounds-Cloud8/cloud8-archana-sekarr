# Project requirements

1. Include best security practises, that have not yet been implemented in the version 1.0.

2. Web server should be accessible only via a proxy and not via a public IP so a loadbalancer is required to satisy this requirement.

3. Should a user connect to the load balancer via HTTP, this connection should be automatically upgraded to HTTPS.

4. The connection must be secured with at least TLS 1.2 or higher.

5. The web server must undergo a health check on a regular basis so the loadbalancer performs these checks.

6. Should the web server fail this health check, the server should be automatically restored.

7. If the the web server has continuous high load, additional servers should be launched. 

8. The customer believes that no more than 3 servers in total are ever needed, given the user numbers in the past.


![01_Project_Requirements_v.1.1](../../../00_includes/PROJECT_01/Project-blue-Page-1.drawio_final1.png)

## Forecast for the upcoming design:

- Need to update the security groups and NACLs to satisfy the best security practise requirements.

- Create private subnets 

- A loadbalancer

- Auto-scaling groups

- Health checks on the load balancer

- A certification manager is required 


## Updated versions of the following documents:

- Architectural drawing

- Design documentation

- Decision documentation
