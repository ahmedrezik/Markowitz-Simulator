import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt
import re
import os


tickers = eval(input("\x1b[1;32m Enter the underlying stock trading ticker separated by whiteSpace \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))
stockData = {}
for ticker in tickers.split():
    stockData[ticker] =(pd.DataFrame(yf.download(ticker, start="1999-01-01", end="2021-01-01")))


# ! if file exists read csv instead of donbwlaoding the data 

# data.to_csv(r'/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/ford.csv', index = True)

def annualReturn(ticker):
    annual_Return = stockData[ticker]['Adj Close'].resample('Y').ffill().pct_change()
    plotData(annual_Return,"Yearly",ticker,"Percent","Date")

def MonthlyNetReturn(ticker):
    monthly_returns = stockData[ticker]['Adj Close'].resample('M').ffill().pct_change()
    plotData(monthly_returns,"Monthly",ticker,"Percent","Date")

def DailyNetReturn(ticker):
    daily_returns = stockData[ticker]['Adj Close'].pct_change()
    print(daily_returns.mean())
    plotData(daily_returns,"Daily",ticker,"Percent","Date")

def CumlativeReturn(period,ticker):
    if period == "D":
        daily_returns = stockData[ticker]['Adj Close'].pct_change()
        cum_returns = (daily_returns + 1).cumprod()

    elif period == "Y":
        annual_Return = stockData[ticker]['Adj Close'].resample('Y').ffill().pct_change()
        cum_returns = (annual_Return + 1).cumprod()

    elif period == "M":
        monthly_returns = stockData[ticker]['Adj Close'].resample('M').ffill().pct_change()
        cum_returns = (monthly_returns + 1).cumprod()
    
    plotData(plotData,"cumulative returns data",ticker,"Growth of $1 investment","Date")
   

def plotData(dataFrame,ReturnPeriod,tickerName,ylabel,xlabel):
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    ax1.plot(dataFrame)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_title(tickerName + " " + ReturnPeriod)
    plt.show()   


CumlativeReturn("M","tsla")

#! tech_stocks = ['AAPL', 'MSFT', 'INTC']
#! bank_stocks = ['WFC', 'BAC', 'C']
#! commodity_futures = ['GC=F', 'SI=F', 'CL=F']
#! cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
#! currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
#! mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
#! us_treasuries = ['^TNX', '^IRX', '^TYX']