import pandas as pd
import logging
from typing import Tuple

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")

def train(df: pd.DataFrame)-> Tuple[pd.DataFrame, pd.DataFrame]:
    """
        Takes a dataframe and returns a pivot_table and a dataframe of average salary
    """
    logging.info("creating pivot table and converting to numpy")
    pivot_table = pivot_table = pd.pivot_table(df,index=['club_name'],values = df.drop(['league_name','club_name','contribution_type','wage_eur'],axis=1).columns, aggfunc='median')
    avg_wage = df.drop(['league_name'],axis = 1).groupby('club_name').mean()['wage_eur']
    
    return pivot_table, avg_wage

if __name__ == "__main__":
    print(train(pd.read_csv("./final_data.csv")))