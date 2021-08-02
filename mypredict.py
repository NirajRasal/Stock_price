#ToDo 

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from sklearn.metrics import mean_squared_error

# Importing the training set
dataset_train = pd.read_csv('INFY_train.csv')
training_set = dataset_train.iloc[:, 5:6].values    #get adjustedClose price


# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)



# Creating a data structure with 60 timesteps and 1 output
X_train = []
y_train = []
for i in range(60, 2557):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)


# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Part 2 - Building the RNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

# Initialising the RNN
model = Sequential()

# Adding the first LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
model.add(Dropout(0.2))

# Adding a second LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50, return_sequences = True))
model.add(Dropout(0.2))

# Adding a third LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50, return_sequences = True))
model.add(Dropout(0.2))

# Adding a fourth LSTM layer and some Dropout regularisation
model.add(LSTM(units = 50))
model.add(Dropout(0.2))

# Adding the output layer
model.add(Dense(units = 1))

# Compiling the RNN
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
model.fit(X_train, y_train, epochs = 100, batch_size = 32)

# Part 3 - Making the predictions and visualising the results

# Getting the real stock price of 
dataset_test = pd.read_csv('INFY_test.csv')     #downloaded from yfinance_test.py file
real_stock_price = dataset_test.iloc[:, 5:6].values     #get open price

# Getting the predicted stock price of 
dataset_total = pd.concat((dataset_train['Adj Close'], dataset_test['Adj Close']), axis = 0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)

X_test = []
for i in range(60, 71):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)

X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = model.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

# TRAINING RMSE
#trainScore = math.sqrt(mean_squared_error(y_train[0], trainPredict[:,0]))
#print('Train RMSE: %.2f' % (trainScore))

# TEST RMSE
#testScore = math.sqrt(mean_squared_error(X_test[0], predicted_stock_price[:,0]))
#print('Test RMSE: %.2f' % (testScore))

# Visualising the results
plt.plot(real_stock_price, color = 'red', label = 'Real INFY Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted INFY Stock Price')
plt.title('INFY Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('INFY Stock Price')
plt.legend()
plt.show()
