import pandas as pd
import logging
from typing import Tuple
import os

def setup_logger():
    if os.getenv('RUNNING_IN_DOCKER'):
        log_dir = "/app/logs"
        os.makedirs(log_dir, exist_ok=True)
        logging.basicConfig(filename=os.path.join(log_dir, 'app.log'),
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")
        logger = logging.getLogger(__name__)
        return logger
    else:
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.NullHandler())  
        return logger
    
logger = setup_logger()

def train(df: pd.DataFrame)-> Tuple[pd.DataFrame, pd.DataFrame]:
    """
        Takes a dataframe and returns a pivot_table and a dataframe of average salary
    """
    logger.info("creating pivot table and converting to numpy")
    pivot_table = pd.pivot_table(df,index=['name'],values = df.drop(['league_name','club_name','wage_eur','name'],axis=1).columns)
    avg_wage = df.drop(['league_name','name'],axis = 1).groupby('club_name').mean()['wage_eur']
    return pivot_table, avg_wage

if __name__ == "__main__":
    print(train(pd.read_csv("../dataset/data.csv")))