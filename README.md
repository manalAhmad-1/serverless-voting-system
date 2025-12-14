**Serverless Voting System**
--
**Course Information:**

- **Course:** Cloud Computing

- **Instructor:** Dr. Ahmed Nasrallah

- **Department:** Computer Engineering

- **University:** Kuwait University – College of Engineering & Petroleum


**Team Members:**

- Fatma Al Rashidi
- Manal Alelaiwi
- Ahed Alotaibi

**Project Overview:**

The Serverless Voting System is a cloud-based web application that allows users to create polls, vote on available options, and view results in real time.
The system is fully serverless and uses AWS managed services to ensure scalability, reliability, and low operational cost.

**Features:**

- Create a new poll with a title and multiple options
- Automatically generated Poll ID for voting and results
- Submit votes for any poll
- Optional comments during voting
- Real-time results display
- Email notification sent automatically when a new poll is created (SNS Bonus Feature)
- Simple frontend built using HTML and JavaScript

**AWS Services Used:**

**AWS Lambda:**
Handles all backend logic for:

- Creating polls
- Retrieving poll details
- Submitting votes
- Returning poll results

**Amazon API Gateway:**

- Provides REST API endpoints for the frontend
- Routes requests to the correct Lambda functions

**Amazon RDS (MySQL):**

- Stores poll information, options, and votes
- Provides structured relational data storage

**Amazon SNS (Bonus):**

- Sends automatic email notifications whenever a new poll is created
- Demonstrates use of event-driven architecture

**IAM and CloudWatch:**

- IAM roles secure Lambda and database access
- CloudWatch used for execution logs and debugging

**System Architecture:**

- The user interacts with the HTML/JavaScript frontend
- The frontend communicates with API Gateway
- API Gateway triggers Lambda functions
- Lambda functions read and write data to Amazon RDS (MySQL)-When a poll is created, Lambda publishes a message to Amazon SNS
- SNS sends an automatic email notification to the subscribed email
- Results are returned to the frontend for display

**API Endpoints**

**POST /polls:**
- Creates a new poll

**GET /polls/{id}:**
- Returns poll title and options

**POST /polls/{id}/vote:**
- Submits a vote with an optional comment

**GET /polls/{id}/results:**
- Returns total votes and percentages

**How to Use the Application:**

1. Open the frontend (AWS Amplify hosting or local index.html)
2. Enter a poll title and comma-separated options
3. Click "Create Poll"
4. Copy the generated Poll ID
5. Use the Poll ID to load the poll, vote, or view results
6. When a poll is created, an email notification is automatically sent through SNS


**Testing Summary:**

- Poll creation successfully verified
- Poll ID generation and auto-fill confirmed
- Voting functionality tested
- Result calculations display correctly
- SNS email notifications tested and received
- Frontend and backend integration confirmed

**Conclusion:**

This project demonstrates how AWS serverless technologies can be used to build a scalable, reliable, and low-cost web application.
All course requirements have been met, and an additional SNS notification feature was implemented as a bonus to demonstrate event-driven design.

**Notes:**

- The project uses only AWS managed services
- No servers are required

- Architecture is highly scalable and efficient





