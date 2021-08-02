#nsepy looks usefull
from datetime import date
from nsepy import get_history
import matplotlib.pyplot as plt 
import pandas as pd

ticker = get_history(symbol='TCS',start=date(2020,9,2),end=date(2020,9,15))

ticker.to_csv('tcs_test_modified.csv')
#print(ticker)

#pricee = sbin['Close']  not working
#print(pricee)
#pricee.plot(x='days',y='price',kind='line')
#sbin[['Close']].plot()