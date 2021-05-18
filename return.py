import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt
import re
import os


# ! List of Tickers 
# ! Donwload and then use csv
# ! CSV and function to run on the data
tickers = eval(input("\x1b[1;32m Enter the underlying stock trading ticker separated by whiteSpace \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))
stockData = {}
for ticker in tickers.split():
    stockData[ticker] =(pd.DataFrame(yf.download(ticker, start="1999-01-01", end="2021-01-01")))


# ! if file exists read csv instead of donbwlaoding the data 

# data.to_csv(r'/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/ford.csv', index = True)

def annualReturn(ticker):
    annual_Return = stockData[ticker]['Adj Close'].resample('Y').ffill().pct_change()
    plotData(annual_Return,"Yearly",ticker)

def MonthlyNetReturn(ticker):
    monthly_returns = stockData[ticker]['Adj Close'].resample('M').ffill().pct_change()
    plotData(monthly_returns,"Monthly",ticker)

def DailyNetReturn(ticker):
    daily_returns = stockData[ticker]['Adj Close'].pct_change()
    print(daily_returns.mean())
    plotData(daily_returns,"Daily",ticker)

def plotData(dataFrame,ReturnPeriod,tickerName):
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    ax1.plot(dataFrame)
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Percent")
    ax1.set_title(tickerName + " " + ReturnPeriod)
    plt.show()

# ! Add ability to choose cumulative periods
def CumulativeReturn():
    daily_returns = data['Adj Close'].pct_change()
    cum_returns = (daily_returns + 1).cumprod()
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    cum_returns.plot()
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Growth of $1 investment")
    ax1.set_title(ticker +"daily cumulative returns data")
    plt.show()
    


DailyNetReturn("tsla")
