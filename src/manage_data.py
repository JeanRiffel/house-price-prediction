import pandas as pd

def getData():
  return pd.read_csv('data/fake_house_prices_dataset.csv')
  


def generateData():
  return pd.DataFrame({'bedrooms': [2,3,5,2]})
  