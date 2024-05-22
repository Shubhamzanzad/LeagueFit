from fastapi import FastAPI,HTTPException, Request
from pydantic import BaseModel
from train import train
from recommend import recommend
import pandas as pd
from typing import List,Union
import uvicorn
from io import StringIO, BytesIO
import requests
import logging
import os

log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'app.log'),
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")


class NumberList(BaseModel):
    numbers: List[Union[float,int]]

class Attributes(BaseModel):
    overall : float
    potential : float
    wage_eur : float
    age : float
    height_cm : float
    weight_kg : float
    international_reputation : float
    pace : float
    shooting : float
    passing : float
    dribbling : float
    defending:float
    physic  : float
    contribution_type : float
    league_name : str
    club_name: str
    name:str
    attacking : float
    skill : float
    power : float
    mentality : float
    goalkeeping  : float
    movement : float

app = FastAPI()

@app.post("/recommend")
def _recommend(data:NumberList):
    logging.info("posting attributes")
    if not data.numbers:
        logging.error("Empty list")
        raise HTTPException(status_code=400, detail="The list of numbers is empty.")
    
    response = requests.get("http://dataset:8008/getDf")
    response.raise_for_status()
    
    df = pd.read_csv(StringIO(response.text))

    pivot_table, avg_wage = train(df)
    teams = recommend(df,data.numbers,5,pivot_table,avg_wage)
    k=1
    for index, row in teams.iterrows():
        club_name = row['club_name']
        wage_eur = row['wage_eur']
        logging.info(f"Recommended Team {k} - club name: {club_name} - average wage: {wage_eur}")
        k+=1 
    
    return teams.to_dict(orient='records')

@app.post("/addPlayer")
def _addPlayer(attributes:Attributes):
    logging.info(f"getting attributes")
    if not attributes:
        logging.error("Empty attribute")
        raise HTTPException(status_code=400, detail="Attributes is empty.")
    response = requests.get("http://dataset:8008/getDf")
    response.raise_for_status()
    df = pd.read_csv(StringIO(response.text))
    
    new_row = pd.DataFrame([attributes.dict()])
    new_row['league_name'] = df[df['club_name']==new_row['club_name'][0]]['league_name'].iloc[0]
    df = pd.concat([df,new_row],ignore_index=True)

    logging.info(f"accepted recommendation - club name: {new_row['club_name'][0]}, average wage: {new_row['wage_eur'][0]}")
    
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    
    logging.info("posting to store to dataframe")
    
    response = requests.post(
        "http://dataset:8008/addPlayer",
        files={"file": ("data.csv", csv_buffer, "text/csv")}
    )
    response.raise_for_status()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
