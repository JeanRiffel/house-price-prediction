from src import manage_data, manage_model, show_data

data = manage_data.getData()

X = data[['bedrooms']]
y = data['price']

manage_model.trainModel(X, y)
newData = manage_data.generateData()
predictions = manage_model.getPredictions(newData)

newData['prices_predict'] = predictions
bedrooms_list = newData['bedrooms'].tolist()
prices_predict_array = newData['prices_predict'].to_numpy()

show_data.printData(data, bedrooms_list, prices_predict_array)
