import pandas as pd
import logging
from typing import Tuple
import os

log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'app.log'),
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")

def train(df: pd.DataFrame)-> Tuple[pd.DataFrame, pd.DataFrame]:
    """
        Takes a dataframe and returns a pivot_table and a dataframe of average salary
    """
    logging.info("creating pivot table and converting to numpy")
    pivot_table = pd.pivot_table(df,index=['name'],values = df.drop(['league_name','club_name','wage_eur','name'],axis=1).columns)
    avg_wage = df.drop(['league_name','name'],axis = 1).groupby('club_name').mean()['wage_eur']
    return pivot_table, avg_wage

if __name__ == "__main__":
    print(train(pd.read_csv("../dataset/data.csv")))