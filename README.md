# Mock Test Portal for Training Basket

## Overview

The Mock Test Portal is a web-based assessment platform developed for **Training Basket** to conduct online mock tests for students across multiple technology domains. The platform enables students to attempt technology-specific examinations, receive instant results, and allows trainers to track performance through centralized result storage using Google Sheets.

The application is built using **Python Flask** and is designed to be lightweight, easy to deploy, and simple to manage without requiring a dedicated database server.

---

## Features

### Student Information Collection

Students provide:

* Name
* Enrollment Number
* Batch Number
* Trainer Name
* Course Selection

### Technology-Based Assessments

Currently supported domains:

* Data Analytics (DA)
* Data Science (DS)
* AWS Cloud (CLOUD)

Each domain has its own question bank stored in JSON format.

### Online Examination System

* Multiple-choice questions (MCQs)
* Single-answer selection
* Automated score calculation
* Percentage-based evaluation
* Instant result generation

### Timer-Based Assessment

* Configurable exam timer
* Automatic submission when time expires
* Fair and controlled examination environment

### Result Management

Student results are automatically stored in Google Sheets with:

* Student Name
* Enrollment Number
* Batch Number
* Trainer Name
* Course Name
* Score
* Percentage
* Attempt Timestamp

### Cloud-Based Storage

Instead of maintaining a local database, the application integrates directly with Google Sheets for:

* Easy access
* Centralized reporting
* Real-time updates
* Trainer visibility

---

## Technology Stack

### Backend

* Python
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### Data Storage

* Google Sheets API
* Google Service Account Authentication

### Deployment

* Railway
* GitHub

---

## Project Structure

```text
mock_test_portal/
│
├── app.py
├── credentials.json
├── requirements.txt
├── Procfile
│
├── data/
│   ├── da_questions.json
│   ├── ds_questions.json
│   └── cloud_questions.json
│
└── templates/
    ├── home.html
    ├── exam.html
    └── result.html
```

---

## Application Workflow

### Step 1

Student opens the portal.

### Step 2

Student enters:

* Name
* Enrollment Number
* Batch Number
* Trainer Name

### Step 3

Student selects the desired technology exam.

### Step 4

The examination starts with a timer.

### Step 5

Student submits the exam or the timer auto-submits.

### Step 6

The system:

* Evaluates answers
* Calculates score
* Calculates percentage

### Step 7

Results are:

* Displayed immediately
* Stored in Google Sheets

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will be available at:

```text
http://127.0.0.1:5000
```

---

## Google Sheets Integration

### Create Google Cloud Project

1. Create a Google Cloud Project
2. Enable:

   * Google Sheets API
   * Google Drive API
3. Create a Service Account
4. Download credentials JSON

### Share Sheet

Share the Google Sheet with the Service Account email and grant **Editor** access.

### Update Credentials

Place the credentials file in the project root directory or configure through environment variables during deployment.

---

## Use Cases

### For Students

* Practice placement-oriented mock tests
* Evaluate technical knowledge
* Identify strengths and weaknesses

### For Trainers

* Track student performance
* Monitor batch-wise progress
* Generate performance reports

### For Training Institutes

* Conduct online assessments
* Standardize evaluation processes
* Maintain centralized result records

---

## Future Scope

### User Authentication

* Student Login
* Trainer Login
* Admin Login

### Trainer Dashboard

* View student attempts
* Filter by trainer
* Filter by batch
* Export reports

### Admin Dashboard

* Manage question banks
* Add/Edit/Delete exams
* Manage trainers
* Manage batches

### Advanced Analytics

* Student ranking
* Batch-wise ranking
* Trainer-wise performance reports
* Accuracy trends
* Progress tracking

### Certificate Generation

* Automatic certificate generation
* PDF download
* Performance-based certification

### Leaderboard System

* Top performers
* Batch rankings
* Technology-wise rankings

### Question Management Portal

* Upload questions through UI
* Import from Excel
* Bulk question upload

### Examination Security

* Question randomization
* Option randomization
* Browser tab switching detection
* Full-screen examination mode

### AI-Powered Features

* Personalized feedback
* Weak-topic identification
* AI-generated practice questions
* Adaptive assessments

### Database Integration

Future migration to:

* SQLite
* PostgreSQL
* MySQL

for large-scale deployment.

### Multi-Technology Expansion

Additional examination domains:

* Python
* SQL
* Machine Learning
* Deep Learning
* Generative AI
* Agentic AI
* Power BI
* Tableau
* Networking
* Cyber Security
* DevOps
* Azure
* Google Cloud Platform

---

## Developed For

**Training Basket**

This project was developed to provide a simple, scalable, and effective mock examination platform for students preparing for placement opportunities and technical interviews across Data Analytics, Data Science, Cloud Computing, and emerging technology domains.

---

## Author

**Tushar Khitoliya**

AI/ML Engineer | Data Science Trainer | Generative AI Enthusiast

Training Basket
