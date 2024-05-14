from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from train import train
from recommend import recommend
import pandas as pd
from typing import List,Union
import uvicorn
import io
import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")


class NumberList(BaseModel):
    numbers: List[Union[float,int]]

app = FastAPI()

@app.post("/recommend")
def _recommend(data:NumberList):
    logging.info("posting attributes")
    if not data.numbers:
        raise HTTPException(status_code=400, detail="The list of numbers is empty.")
    response = requests.get("http://dataset:80/final_data.csv")
    df = pd.read_csv(io.StringIO(response.text))
    
    # Convert NumberList object to dictionary before sending in the request
    pivot_table, avg_wage = train(df)
    teams = recommend(data.numbers,5,pivot_table,avg_wage)
    logging.info("recommending teams")
    return teams.to_dict(orient='records')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
