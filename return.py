import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt
import re


ticker = eval(input("\x1b[1;32m Enter the underlying stock trading ticker \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))
tkr = yf.Ticker(ticker)
data = pd.DataFrame(tkr.history(period="max")) 
data.to_csv(r'/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/aaple.csv', index = True)
data['Close'].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted")
plt.title(ticker+"Price data")
plt.show()
def DailyNetReturn():
    daily_returns = data['Close'].pct_change()
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    ax1.plot(daily_returns)
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Percent")
    ax1.set_title(ticker + "daily returns data")
    plt.show()

def MonthlyNetReturn():
    monthly_returns = data['Close'].resample('M').ffill().pct_change()
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    ax1.plot(monthly_returns)
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Percent")
    ax1.set_title(ticker +"monthly returns data")
    plt.show()

def CumulativeReturn():
    daily_returns = data['Close'].pct_change()
    cum_returns = (daily_returns + 1).cumprod()
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    cum_returns.plot()
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Growth of $1 investment")
    ax1.set_title(ticker +"daily cumulative returns data")
    plt.show()
    

def logReturn():
    ClosingPrice = []
    for i in range(20):
        ClosingPrice.append(data["Close"][str(2000+i)][0])

    logReturn = []
    years = []
    for i in range(19):
        logReturn.append(np.log(ClosingPrice[i+1]/ClosingPrice[i]))
        years.append(str(2000+i))
    plt.plot(years,logReturn)
    plt.show()


