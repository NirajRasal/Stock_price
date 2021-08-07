#nsepy looks usefull
from datetime import date
from nsepy import get_history
import matplotlib.pyplot as plt 
import pandas as pd

today = date.today()            #get today's date

#save_path = 'F:/niraj/Study/Data Science/Stock_price/Data'
symbol = 'idfcfirstb'
ticker = get_history(symbol=symbol,start=date(2021,1,1),end=today)

#ticker.to_csv(symbol+'.csv')

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