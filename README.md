 # Serverless Voting System


 **Course Information**

- **Course:** Cloud Computing  
- **Instructor:** Dr. Ahmed Nasrallah  
- **Department:** Computer Engineering  
- **University:** Kuwait University – College of Engineering & Petroleum  

**Team Members**

- Fatma Al Rashidi  
- Manal Alelaiwi  
- Ahed Alotaibi  



**Project Overview**

The **Serverless Voting System** is a cloud-based web application that allows users to create polls, vote on available options, and view results in real time.  
The system is implemented using a **fully serverless architecture** on AWS, leveraging managed cloud services to ensure scalability, reliability, and low operational cost without managing servers.



**Features**

- Create a new poll with a title and multiple options  
- Automatically generated **Poll ID** for voting and result retrieval  
- Submit votes for any active poll  
- Real-time results display with vote percentages  
- **Email notification sent automatically when a new poll is created (SNS Bonus Feature)**  
- Simple frontend built using **HTML and JavaScript**  
- Fully serverless backend architecture  

**AWS Services Used:**

**Amazon S3**
- Hosts the frontend as a **static website**
- Stores HTML and JavaScript files
- Provides public access to the web interface via a browser

**AWS Lambda**
Handles all backend logic, including:
- Creating polls  
- Retrieving poll details  
- Submitting votes  
- Calculating and returning poll results  

Each operation is implemented as a **separate Lambda function** to ensure modularity and scalability.

**Amazon API Gateway**
- Provides RESTful API endpoints
- Routes frontend requests to the appropriate Lambda functions
- Acts as the communication layer between frontend and backend

### Amazon RDS (MySQL)
- Stores poll information, options, and votes
- Provides structured relational data storage
- Ensures data persistence and consistency

**Amazon SNS (Bonus / Innovation Feature)**
- Sends automatic email notifications when a new poll is created
- Demonstrates **event-driven architecture**
- Adds an innovative cloud-based notification feature

**AWS IAM and CloudWatch**
- IAM roles secure access between AWS services
- CloudWatch is used for logging, monitoring, and debugging Lambda executions


**System Architecture**

- The user interacts with the **HTML/JavaScript frontend hosted on Amazon S3**
- The frontend sends HTTP requests to **Amazon API Gateway**
- API Gateway invokes the appropriate **AWS Lambda function**
- Lambda functions read from and write to **Amazon RDS (MySQL)**
- When a poll is created, the Lambda function publishes a message to **Amazon SNS**
- SNS sends an automatic email notification to the subscribed email address
- The backend returns responses to the frontend for display


**API Endpoints**

**POST /polls**
- Creates a new poll with a title and options

**GET /polls/{id}**
- Retrieves poll title and available options

**POST /polls/{id}/vote**
- Submits a vote for a selected option

**GET /polls/{id}/results**
- Returns total votes and vote percentages for each option


**How to Use the Application**

1. Open the frontend using the **Amazon S3 static website link**
2. Enter a poll title and comma-separated options
3. Click **Create Poll**
4. Copy the generated **Poll ID**
5. Use the Poll ID to load the poll, submit votes, or view results
6. When a poll is created, an **email notification is automatically sent via SNS**


**Testing Summary**

- Poll creation successfully verified  
- Poll ID generation and auto-fill confirmed  
- Voting functionality tested and validated  
- Result calculations and percentages verified  
- SNS email notifications tested and received  
- Frontend and backend integration confirmed through API Gateway  


**Conclusion**

This project demonstrates how **AWS serverless technologies** can be used to build a **scalable, reliable, and cost-efficient** web application.  
All course requirements have been fulfilled, and an additional **SNS-based notification feature** was implemented as a bonus to demonstrate **event-driven cloud design**.

**Notes**

- The project uses **only AWS managed services**
- No traditional servers are required
- The architecture supports **automatic scalability**
- Operational cost is minimized using serverless components









