
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
    prices = pd.read_csv("clx.csv")['Close']
    prices30 = prices[0:len(prices)-30]


    returns = prices30.pct_change()

    last_price = prices30[len(prices30)-1]

    #Number​ of Simulations
    num_simulations = trials
    num_days = days_in_the_future

    simulation_df = pd.DataFrame()

    for x in range(num_simulations):
        count = 0
        daily_vol = returns.std()
        
        price_series = []
        #Drift
        price = last_price * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        
        for y in range(num_days):
            if count == 251:
                break
            #shock0
            price = price_series[count] * (1 + np.random.normal(0, daily_vol))
            price_series.append(price)
            count += 1
        
        simulation_df[x] = price_series

    print(simulation_df) 
    fig = plt.figure()
    fig.suptitle('Monte Carlo Simulation: AAPL')
    plt.plot(simulation_df.mean(axis=1))
    #plt.axhline(y = last_price, color = 'r', linestyle = '-')
    newdf  = prices[len(prices)-31:len(prices)]
    newdf.reset_index(drop=True, inplace=True)
    print(newdf)
    plt.plot(newdf)
    plt.xlabel('Day')
    plt.ylabel('Price')
    plt.show()


stock_Sim("AAPL",30,10)