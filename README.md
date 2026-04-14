# LeagueFit

## Introduction
LeagueFit is a football club recommendation web application that suggests the top 5 most suitable clubs for a player from the **English Premier League**, **French Ligue 1**, and **German Bundesliga**, based on the player's attributes.

Users input stats like pace, shooting, dribbling, defence, and more through an interactive UI. LeagueFit uses **cosine similarity** on a trained pivot table of club averages to find the best-matching clubs. Users can then accept a recommendation, which adds the player to that club's roster in the live dataset.

The project demonstrates end-to-end DevOps practices including containerization, CI/CD pipelines, automated deployment with Ansible, and centralized logging.

## Architecture

The app runs as three Docker services coordinated by Docker Compose:

- **Dataset service** (`localhost:8008`) — Serves and stores the player dataset via a FastAPI REST API.
- **Backend service** (`localhost:8000`) — Trains the recommendation model on demand and serves predictions via FastAPI.
- **Frontend service** (`localhost:8501`) — Streamlit UI where users input player attributes and view recommended clubs.

```
User → Streamlit Frontend → FastAPI Backend → FastAPI Dataset Service
                                          ↑ (reads/writes CSV data)
```

## Technologies Used

| Layer | Technology |
|---|---|
| Frontend | Python, Streamlit |
| Backend | Python, FastAPI, Uvicorn |
| Recommendation Engine | Python, Scikit-learn (cosine similarity) |
| Dataset API | Python, FastAPI |
| CI/CD Pipeline | Jenkins |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Automation | Ansible |
| Logging | Python logging (file-based, shared volume) |

## Running Locally

**Prerequisites:** Docker and Docker Compose installed.

1. Clone the repository:

   ```bash
   git clone https://github.com/SiddharthVPillai/LeagueFit.git
   cd LeagueFit
   ```

2. Start all three services:

   ```bash
   docker-compose up
   ```

3. Open `http://localhost:8501` in your browser to use the app.

4. To inspect the dataset API or test endpoints, visit `http://localhost:8008/docs`.

   To verify recommendations are being saved, run the `/check` endpoint from the Swagger UI.

## How It Works

1. Enter player attributes (age, pace, shooting, dribbling, etc.) using the sliders.
2. Click **Get Recommendations** — the backend trains a cosine similarity model on current club averages and returns the top 5 matching clubs.
3. Click **Accept Recommendation** to add a fictional player with those attributes to the chosen club's dataset.

> See [DEPLOY.md](DEPLOY.md) for free cloud deployment instructions.
