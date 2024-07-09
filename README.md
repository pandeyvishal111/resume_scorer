# CV Matching Scorer API

## Overview
This API scores a resume based on its relevance to a given job description using a pre-trained BERT model.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install flask transformers torch
3. run python file:
    python app.py  
4. Example curl:
    curl --location 'http://127.0.0.1:5000/score' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=vxOeqAcX7QXlDAi93ApRUEo079xsJqbPXZpAvWZHyrFZehemapmLxzsSRgn26ts0' \
--data-raw '{"job_description": 
"Hands-on experience in developing AI and machine learning solutions.Proficiency in programming languages such as Python, R, or Java, and familiarity with AI libraries/frameworks (e.g.,TensorFlow PyTorch, scikit-learn).Strong understanding of machine learning algorithms and statistical methods.Experience with data pre-processing, feature engineering, and model evaluation techniques.Excellent problem-solving skills and the ability to work independently or as part of a team.Effective communication skills with the ability to translate technical concepts into business terms.Experience with cloud platforms (e.g., AWS, Azure) and big data technologies is a plus.Experience in Model fine-tuning, RAG, and building AI Agents.Hands-on with Large language models and Small language models.",
"resume":"VISHAL PANDEY.Contact Information:Phone: 8376856373.Email: vishalpandey.aset@gmail.com.Summary:Experienced Technology Lead specialising in Analytics with expertise in implementing innovative solutions across diverse projects. Proficient in a wide range of technologies, including cloud services, database management, AI integration, and software development. Proven ability to lead teams and drive successful project outcomes. Currently serving as a Lead Data Scientist at Infocom Network Limited.Skills:Programming Languages: Python, SQL.Cloud Services: AWS, GCP.Database Management: PostgreSQL, DynamoDB, Aurora Serverless DB.DevOps: Jenkins, Kubernetes.Version Control: Git, Bitbucket.Tools: Tableau, DataStudio, Metabase, Quicksight, Jira, VS Code.Web Frameworks: FastAPI, Django.Operating Systems: Linux.Others: CI/CD, Elastic Search"}'
