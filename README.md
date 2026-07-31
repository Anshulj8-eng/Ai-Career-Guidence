# AI Career Guidance System 🚀

## Overview

AI Career Guidance System is an intelligent web application that helps students and job seekers analyze their skills, identify skill gaps, receive career recommendations, and interact with an AI-powered chatbot for personalized guidance.

The platform uses Artificial Intelligence and Machine Learning techniques to provide career suggestions based on the user's resume and target job role.

---

## Features

### 📄 Resume Analysis

* Upload your resume in PDF format.
* Extract skills automatically from the resume.
* Display the extracted information.

### 📊 Skill Gap Analysis

* Compare your current skills with your desired job role.
* Identify missing skills.
* Get suggestions for improvement.

### 💼 Job Recommendations

* Receive job recommendations based on your skills.
* Explore career paths and opportunities.

### 🤖 AI Chatbot Assistant

* Ask career-related questions.
* Get personalized learning recommendations.
* Receive interview preparation guidance.

### 📈 Dashboard

* Visualize your skills using charts and graphs.
* Track your career progress.

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite
* MySQL

### Data Science and AI

* Pandas
* NumPy
* Scikit-learn
* Machine Learning

### Visualization

* Matplotlib
* Chart.js

### AI Tools

* LangChain
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)

---

## Project Structure

```text
AI_Career_Guidance/

├── back/
│   ├── app.py
│   ├── chatbot.py
│   ├── resume_parser.py
│   ├── recommendation.py
│   ├── skill_gap.py
│   ├── requirements.txt
│   ├── templates/
│   └── static/
│
├── Database/
│   └── database.db
│
├── venv/
│
├── .gitignore
├── README.md
└── LICENSE
```
# 🏗️ System Architecture

```text
                                    ┌──────────────────┐
                                    │      User        │
                                    └────────┬─────────┘
                                             │
                                             ▼
                         ┌──────────────────────────────────┐
                         │        Frontend Interface        │
                         │     (HTML, CSS, JavaScript)      │
                         └────────────────┬─────────────────┘
                                          │
                                          ▼
                         ┌──────────────────────────────────┐
                         │          Flask Backend           │
                         │            (app.py)              │
                         └────────────────┬─────────────────┘
                                          │
            ┌─────────────────────────────┼─────────────────────────────┐
            │                             │                             │
            ▼                             ▼                             ▼

 ┌──────────────────┐      ┌──────────────────────┐      ┌──────────────────┐
 │  Resume Parser   │      │   Skill Gap Engine   │      │   AI Chatbot     │
 │ (resume_parser)  │      │    (skill_gap.py)    │      │   (chatbot.py)   │
 └────────┬─────────┘      └──────────┬───────────┘      └────────┬─────────┘
          │                            │                           │
          └────────────────────────────┼───────────────────────────┘
                                       │
                                       ▼
                      ┌────────────────────────────────┐
                      │     Recommendation Engine      │
                      │    (recommendation.py)         │
                      └────────────────┬───────────────┘
                                       │
                                       ▼
                      ┌────────────────────────────────┐
                      │      SQLite Database           │
                      │     Database/database.db       │
                      └────────────────┬───────────────┘
                                       │
                                       ▼
                      ┌────────────────────────────────┐
                      │      Career Suggestions        │
                      │  Jobs • Skills • Roadmaps      │
                      └────────────────────────────────┘
```

---

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/AI_Career_Guidance.git
```

### Step 2: Move to the project directory

```bash
cd AI_Career_Guidance
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open the browser

```text
http://127.0.0.1:5000
```
# Activate the virtual environment

# Windows
venv\Scripts\activate

# Install dependencies
pip install -r back/requirements.txt

# Run the project
python back/app.py
---

---

## Use Cases

* Students
* Freshers
* Job seekers
* Career counselors
* Colleges and universities

---

## Author

**Anshul**

B.Tech (Artificial Intelligence & Data Science)

---

## License

This project is intended for educational and learning purposes.
