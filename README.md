# QA Pizza Restaurant

You've been tasked with setting up a website for a local pizzeria using AWS and docker

AWS Requirements:
- VPC
- Subnets
- IGW
- Route Table
- Security Groups
- Load Balancer
- EC2s
- RDS

Software Requirements:
- Each of the EC2s have docker installed
- Git clone down this repo
- Container for application
- Container for nginx
- RDS for database

Project Specifics

Create a dockerfile for the application container, modifying the code where necessary for use with your RDS. 
Create the nginx container modifying the nginx.conf either through a mount or through modifying the file. 
Create the RDS manually and use the create.sql file to populate the database. 
Make sure the application talks to the RDS and no security concerns.

Using a load balancer, create two instances of your application and ensure there is a difference between the code hosted between the VMs, whether its just by slightly modifying the index.html
