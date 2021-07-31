#nsepy looks usefull
from datetime import date
from nsepy import get_history
import matplotlib.pyplot as plt 
import pandas as pd

ticker = get_history(symbol='INFY',start=date(2015,7,1),end=date(2021,8,1))

#sbin.to_csv('cdsl.csv') working
print(ticker)

#pricee = sbin['Close']  not working
#print(pricee)
#pricee.plot(x='days',y='price',kind='line')
#sbin[['Close']].plot()