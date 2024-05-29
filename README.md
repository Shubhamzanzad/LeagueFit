# LeagueFit

## Introduction
LeagueFit is a web application that helps users find the top 5 most similar clubs from English Premier League, French League 1 and German 1. Bundesliga based on player attributes. 
This application uses cosine similarity to find the club names of 5 most similar players.
In this project, we used DevOps practices like pipeline creation, containerization and orchestration, monitoring etc.

## Technologies Used
- **Frontend** - Python (Streamlit)
- **Backend** - Python (FastAPI and Uvicorn)
- **Recommendation System** - Python (Sklearn)
- **CI/CD Pipeline** - Jenkins
- **Containerization** - Docker
- **Container Orchestration** - Docker compose
- **Automation** - Ansible

## Installing and Running
To run **LeagueFit** locally, follow these steps:
1. Clone the repository:
   
   ```bash
   git clone https://github.com/SiddharthVPillai/LeagueFit.git
   cd LeagueFit
   ```
3. Run the docke compose file to run the frontend, backend and dataset containers:
   
    ```bash
      docker-compose up
    ```
4. On your web browser goto `localhost:8501`. You will reach the main page of the application as shown below.
   
   ![image](https://github.com/SiddharthVPillai/LeagueFit/assets/68557526/4ddb17dc-a44f-4da6-8fa3-435ee4c6d2b8)

   In order to test whether the recommendation is added to the dataframe, goto `localhost:8008/docs` on your web browser and run the `/check` end point.

   ![image](https://github.com/SiddharthVPillai/LeagueFit/assets/68557526/5d939247-61c2-4018-9bca-f0153a7b8e0e)
