from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from train import train
from recommend import recommend
import pandas as pd
from typing import List,Union
import uvicorn
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
    path = "./final_data.csv"
    pivot_table,avg_wage = train(pd.read_csv(path))
    
    logging.info("recommending teams")
    teams = recommend(data.numbers,5,pivot_table,avg_wage)
    return teams.to_dict(orient='records')

if __name__ == "__main__":
    uvicorn.run(app)