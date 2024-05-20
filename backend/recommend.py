import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from train import train
import requests
import logging
import os

log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'app.log'),
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")

def recommend(df: pd.DataFrame ,vec: list[int], k: int, pivot_table: pd.DataFrame, avg_wage: pd.DataFrame) -> pd.DataFrame:
    """
    Takes a vector(attribute vector), avg_wage, pivot_table, and k (number of recommendations) and recommends k teams 
    """
    logging.info("Taking pivot table, avg_wage dataframes and player attributes and recommending k teams")
    np_vec = np.array(vec).reshape(1, -1)
    cs = cosine_similarity(np_vec, pivot_table.to_numpy())
    pd_cs = pd.DataFrame(cs.T,index=pivot_table.index,columns=['cosine_similarity'])
    pd_cs = pd_cs.nlargest(1000,'cosine_similarity').reset_index()
    
    merge_df = pd_cs.merge(df,how='left',left_on='name',right_on='name')
    req = merge_df[['name','cosine_similarity','club_name']]
    
    wage_df = avg_wage.reset_index()
    final = req.merge(wage_df,how='left',left_on='club_name',right_on='club_name')
    
    i = k
    while final.drop(['name','cosine_similarity'],axis=1).head(i).drop_duplicates().shape[0]<k:
        i+=1
    
    return final.drop(['name','cosine_similarity'],axis=1).head(i).drop_duplicates()

if __name__ == "__main__":
    v = [23.0, 59.4, 72.0,75.0, 16.066667, 180.0, 1.0, 64.166667, 68.2, 75.0, 67.0, 67.0, 67.9, 80.0, 65.0, 57.0, 65.0, 74.0]
    response = requests.get("http://localhost:8008/getDf")
    data_json = response.json()
    df = pd.read_json(data_json,orient='records')
    pivot_table, avg_wage = train(df)
    print(recommend(df,v, 5, pivot_table,avg_wage))