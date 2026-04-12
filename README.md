# Automated LinkedIn Post Generator (n8n + FastAPI + React + Postgres)


# Overview

An automated LinkedIn Post Generation system. Keeps track of the already generated posts and creates new, unique posts. Uses tavily to fetch content from blogs and articles to keep accurate facts and statements rather than uttering false claims.
Has two Buttons:
Approve: Publishes the Post on LinkedIn
Reject (Rejection Reason Given): Reiterates the post considering the rejection reason.
Reject (No rejection reason given): Generates a completely new Post.

# Features

- Fully automated post generation pipeline
- Stores previously generated titles in database and reviews them so that duplicate titles are not generated
- Human-in-the-loop approval system
- Real-time post fetching (polling every 3 seconds)
- Develped using local n8n
- Webhook integration with n8n
- Fully containerized deployment
- Hosted on AWS EC2

# Tech Stack

- Frontend: React
- Backend:FastAPI (Python)
- Automation: n8n
- Database: PostgreSQL
- Communication: REST APIs + Webhooks
- Deployment: Docker + AWS EC2

# Project Structure

|-- main.py (FastAPI backend)
|-- frontend/
|  |-- index.html (REACT UI)
|-- docker-compose.yaml (Configuration file used to create and run the containers)
|-- Dockerfile (used to create the image of this app)

# Public URL: http://13.53.65.110:8000/

# Imprtant (When running the worflow for the first time, create the table and a dummy entry in the database so that empty response does not cause error in the workflow)

CREATE TABLE linkedin_posts (
  id SERIAL PRIMARY KEY NOT NULL,
  titles TEXT NOT NULL
);

INSERT INTO linkedin_posts (titles)
VALUES ('First Title');