import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt
import re


ticker = "AAPL"#eval(input("\x1b[1;32m Enter the underlying stock trading ticker \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))
tkr = yf.Ticker(ticker)
data = pd.DataFrame(tkr.history(period="max")) 
data.to_csv(r'/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/aaple.csv', index = True)

def netReturn(date1,date2):
    # Main assumption here is that there are no dividends distributed 
    # price @t / price @t-1  - 1
    return (data["Close"][date2] -  data["Close"][date1]) / data["Close"][date1]


def grossReturn():
    print("HELLO")

ClosingPrice = []
for i in range(20):
    ClosingPrice.append(data["Close"][str(2000+i)][0])

logReturn = []
for i in range(19):
    logReturn.append(np.log(ClosingPrice[i+1]/ClosingPrice[i]))


print(ClosingPrice)
print(logReturn)

    

# print(data['Close']/data['Close'].shift(365))
# data['Log Return'].plot(figsize=(18,5))
# plt.show()

# daily_avg_returns = data['Log Return'].mean()
# print(daily_avg_returns)

# annual_log_returns = data['Log Return'].mean() * 250
# print(annual_log_returns)
