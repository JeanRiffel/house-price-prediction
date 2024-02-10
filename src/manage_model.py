
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

model = LinearRegression()

def trainModel(X, y):
  model.fit(X, y)

def getPredictions(newData):
  return model.predict(newData)