# LinkedIn Automation

Run the below SQL query in n8n if the postgres database is empty:
CREATE TABLE linkedin_posts (
  id     SERIAL PRIMARY KEY NOT NULL,
  titles TEXT NOT NULL
);
INSERT INTO linkedin_posts (titles) VALUES ('First Title');

App is available at: http://13.53.65.110:8000/
