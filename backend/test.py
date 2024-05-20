from recommend import recommend
import unittest
from train import train
import pandas as pd

class testRecommendation(unittest.TestCase):
    df = pd.read_csv("../dataset/data.csv")
    pivot_table, avg_wage = train(df)
    
    def test_messi(self):
        a = recommend(self.df,[34.0,85.8,1.0,28.25,95.0,17.516667,170.0,5.0,73.833333,90.2,93.0,85.0,91.0,65.0,93.0,77.8,92.0,94.0,72.0],1,self.pivot_table,self.avg_wage)['club_name'][0]
        self.assertEqual(a,"Paris Saint-Germain")

    def test_ronaldo(self):
        b = recommend(self.df,[36.0,87.6,1.0,28.5,88.0,18.183333,187.0,5.0,74.333333,85.4,91.0,87.0,80.0,75.0,91.0,87.2,94.0,83.6,83.0],1,self.pivot_table,self.avg_wage)['club_name'][0]
        self.assertEqual(b,"Manchester United")
        
    def test_mbappe(self):
        c = recommend(self.df,[22.0,82.2,1.0,32.0,92.0,15.516667,182.0,4.0,73.5,92.4,91.0,97.0,80.0,77.0,95.0,82.2,88.0,80.8,73.0],1,self.pivot_table,self.avg_wage)['club_name'][0]
        self.assertEqual(c,"Paris Saint-Germain")


if __name__ == '__main__':
    unittest.main()