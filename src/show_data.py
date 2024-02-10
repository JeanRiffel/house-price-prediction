import matplotlib.pyplot as plt

def printData(data, bedrooms_list, prices_predict_array ):
  plt.scatter(data['bedrooms'], data['price'], color='green', label="Original data")
  plt.plot(bedrooms_list, prices_predict_array, color='red', label='Predicted')
  plt.xlabel('Bedrooms')
  plt.ylabel('Price')
  plt.legend()
  plt.show()