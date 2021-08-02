import yfinance as yf

ticker = yf.download('INFY.BO',start="2010-06-02", end="2020-10-15")     #train
ticker.to_csv('INFY_train.csv')

ticker = yf.download('INFY.BO',start="2020-10-16", end="2020-10-31")     #test
ticker.to_csv('INFY_test.csv')
