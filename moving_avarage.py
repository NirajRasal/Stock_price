import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("INFY_train.csv")

close = df['Adj Close']                     #store Adj close of stock in close

rolling_mean = close.rolling(window=200).mean()     #calculate rolling mean of 200 day price

plt.plot(df[['Adj Close']],label="Tcs stock price")     #plot adjused close price
plt.xlabel("Time")
plt.ylabel("Price")
plt.plot(rolling_mean, label='200 Day SMA', color='orange')
plt.show()

#print(rolling_mean.tail())