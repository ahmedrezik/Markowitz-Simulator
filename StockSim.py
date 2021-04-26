#------------------------------------------------------------------------------------#
import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import yfinance as yf


def stock_Sim(ticker,days_in_the_future ,trials):
    style.use('ggplot')
    ticker2 = ticker 
    tkr = yf.Ticker(ticker2)
    prices = pd.DataFrame(yf.download(ticker2, start="1999-01-01", end="2021-01-01"))['Close'] 
    returns = prices.pct_change()

    last_price = prices[-1]

    #Number​ of Simulations
    num_simulations = trials
    num_days = days_in_the_future

    simulation_df = pd.DataFrame()

    for x in range(num_simulations):
        count = 0
        daily_vol = returns.std()
        
        price_series = []
        
        price = last_price * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        
        for y in range(num_days):
            if count == 251:
                break
            price = price_series[count] * (1 + np.random.normal(0, daily_vol))
            price_series.append(price)
            count += 1
        
        simulation_df[x] = price_series
        
    fig = plt.figure()
    fig.suptitle('Monte Carlo Simulation: AAPL')
    plt.plot(simulation_df)
    plt.axhline(y = last_price, color = 'r', linestyle = '-')
    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.show()


stock_Sim("AAPL",252,5)