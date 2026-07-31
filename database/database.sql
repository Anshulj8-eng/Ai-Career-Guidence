CREATE DATABASE career_ai;

USE career_ai;

CREATE TABLE users(

id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100) UNIQUE,
password VARCHAR(255)

);

CREATE TABLE resumes(

id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
resume_name VARCHAR(255),
skills TEXT,
resume_score INT,

FOREIGN KEY(user_id)
REFERENCES users(id)

);

CREATE TABLE chat_history(

id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
user_message TEXT,
bot_response TEXT,

FOREIGN KEY(user_id)
REFERENCES users(id)

);

CREATE TABLE recommendations(

id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
job_role VARCHAR(100),

FOREIGN KEY(user_id)
REFERENCES users(id)

);