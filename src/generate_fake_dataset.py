import pandas as pd

"""
Regions
A-> Better
B-> Good
C-> Not so good
"""

data = {
  'price': [210000.00, 350500.00, 550000.00, 800000.00],
  'bedrooms': [2, 3, 3, 4],
  'regions': ['C', 'B', 'A', 'A']
}

df = pd.DataFrame(data)

df.to_csv('data/fake_house_prices_dataset.csv', index=False)

print(df)
