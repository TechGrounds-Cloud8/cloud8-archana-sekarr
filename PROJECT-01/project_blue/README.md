
# Project version 1:1
This project is implemented to demonstrate the cloud skills acquired in the TechGrounds Cloud Engineering Cohort.

Goal: 
- To automate the deployemnt of an exisiting architecture deployed in AWS leveraging Infrastructure as Code paradigm with CDK
- Implement the project requirements described in [Requirement-Documentation](../Version-1.1/Documentation/01_Project_Requirements_v.1.1.md)

Generated Documentations:
During the course of the implementation the design and the decisions made are documented.
- [Design-Documentation](../Version-1.1/Documentation/02_Design_Documentation.md)
- [Decision-Documentation](../Version-1.1/Documentation/03_Decision_Documentation.md)

## Setting up the local environment: 

[AWS CDK](https://aws.amazon.com/cdk/) is used with [Python](https://www.python.org/) as the programming language
- Installing [Python](https://cdkworkshop.com/15-prerequisites/600-python.html)
- Installing [Node.JS] (https://nodejs.org/en/)
- Installing [AWS CDK](https://cdkworkshop.com/15-prerequisites/500-toolkit.html)
- Install [AWS CLI] https://cdkworkshop.com/15-prerequisites/100-awscli.html

## Installing the project dependencies
- In the main folder of the cdk project 
- Create the python virtual environment
    ```
    python3 -m venv .venv
    ```
- Activate the virtualenv
    ```
    source .venv/bin/activate
    ```
- Install the python dependencies
   ```
   pip install -r requirements.txt
   ```

## Deploying the CDK project
- Create an [AWS account](https://aws.amazon.com/console/)
- Create the [Admin user](https://cdkworkshop.com/15-prerequisites/200-account.html)
- [Configure the credentials] (https://cdkworkshop.com/15-prerequisites/200-account.html#configure-your-credentials)
- [Deploying the project](https://cdkworkshop.com/30-python/20-create-project/500-deploy.html)
    ```
    cdk deploy
    ```

## Architecture Diagram


## To SSH into the webserver via the management server

Instructions are documented [here] (./project_blue/bastionHostConnection.md)
- Follow from step 2.




