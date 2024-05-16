from recommend import recommend
import unittest
from train import train
import pandas as pd

class testRecommendation(unittest.TestCase):
    df = pd.read_csv("../dataset/final_data.csv")
    pivot_table, avg_wage = train(df)
    
    def test_union(self):
        a = recommend([29.0,58.2,68.0,16.400000,188.0,1.0,61.000000,66.6,74.0,66.0,63.9,74.0,76.0,67.8,59.4,57.4,81.0],1,self.pivot_table,self.avg_wage)['team_name'][0]
        self.assertEqual(a,"1. FC Union Berlin")

    def test_monaco(self):
        b = recommend([25.0,64.8,77.0,15.533333,180.0,2.0,67.833333,74.0,78.0,72.0,74.0,77.8,83.0,73.0,67.0,72.0,74.0],1,self.pivot_table,self.avg_wage)['team_name'][0]
        self.assertEqual(b,"AS Monaco")
        
    def test_arsenal(self):
        c = recommend([26.0,64.0,80.0,16.616667,185.0,2.0,70.500000,68.8,80.0,75.4,75.0,76.0,84.0,68.2,68.0,74.4,77.0],1,self.pivot_table,self.avg_wage)['team_name'][0]
        self.assertEqual(c,"Arsenal")


if __name__ == '__main__':
    unittest.main()