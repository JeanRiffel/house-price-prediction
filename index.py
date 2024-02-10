# index.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import joblib

import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('data/fake_house_prices_dataset.csv')

X = data[['bedrooms']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

print('Coeficient ', model.coef_[0])
print('Intercept', model.intercept_)

newData = pd.DataFrame({'bedrooms': [2,3,4,6,9]})
predictions = model.predict(newData)
newData['prices_predict'] = predictions

bedrooms_list = newData['bedrooms'].tolist()
prices_predict_array = newData['prices_predict'].to_numpy()

print('Original', data)
print('New data', newData) 

plt.scatter(data['bedrooms'], data['price'], label='Dados originais')
plt.plot(bedrooms_list, prices_predict_array, color='red', label='Previsoes')
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.legend()
plt.show()

