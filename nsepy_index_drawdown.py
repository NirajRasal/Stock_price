#import libraries
import datetime
from datetime import date
from nsepy import get_history
import matplotlib.pyplot as plt 
from dateutil.relativedelta import relativedelta
import pandas as pd

today = date.today()            #get today's date
year_ago = today - relativedelta(years=1)

symbol = 'NIFTY'
ticker = get_history(symbol=symbol,start=year_ago,end=today,index=True)

ticker.to_csv(symbol+'.csv')

close = ticker['Close']
max_close = close.max()                 #get hightest closing value
print("max close:",max_close)

today_ohlvc = ticker.iloc[-1]
today_close = today_ohlvc['Close']           #get current day row
print("today close:",today_close)

temp = max_close/100
correction = (max_close-today_close) / temp
formated_correction = "{:.2f}".format(correction)       #to get precision till 2 points in correction float variable

print("Drwadown:",formated_correction)

rolling_mean = close.rolling(window=200).mean() 
print("200 DMA is:",rolling_mean.tail(1))
