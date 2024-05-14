import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from train import train
import io
import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")


def recommend(vec: list[int], k: int, pivot_table: pd.DataFrame, avg_wage: pd.DataFrame) -> pd.DataFrame:
    """
    Takes a vector(attribute vector), avg_wage, pivot_table, and k (number of recommendations) and recommends k teams 
    """
    logging.info("Taking pivot table, avg_wage dataframes and player attributes and recommending k teams")
    np_vec = np.array(vec).reshape(1, -1)
    cs = cosine_similarity(np_vec, pivot_table.to_numpy())
    pd_cs = pd.DataFrame(cs.T, index=pivot_table.index, columns=['cosine_similarity'])
    ind = pd_cs.nlargest(k, 'cosine_similarity').index
    wage = avg_wage[ind]
    return pd.DataFrame({'team_name': ind, 'wage_eur': wage}).reset_index(drop=True)

if __name__ == "__main__":
    v = [23.0, 59.4, 72.0, 16.066667, 180.0, 1.0, 64.166667, 68.2, 75.0, 67.0, 67.0, 67.9, 80.0, 65.0, 57.0, 65.0, 74.0]
    response = requests.get("http://dataset:80/final_data.csv")
    df = pd.read_csv(io.StringIO(response.text))
    print(recommend(v, 5, df))