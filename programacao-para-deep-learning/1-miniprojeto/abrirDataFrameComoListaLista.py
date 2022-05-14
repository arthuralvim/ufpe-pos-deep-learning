#https://www.kaggle.com/datasets/crawford/80-cereals/code?resource=download
import pandas as pd
def getCerealData():
  df = pd.read_csv('cereal.csv')
  return df.values.tolist()