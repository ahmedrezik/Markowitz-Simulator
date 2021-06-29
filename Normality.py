# ! Deviations from normality

import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import datetime 
import returns


# tickers = eval(input("\x1b[1;32m Enter the underlying stock trading ticker separated by whiteSpace \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))
# stockData = {}
# for ticker in tickers.split():
#     stockData[ticker] =(pd.DataFrame(yf.download(ticker, start="1999-01-01", end="2021-01-01")))

def is_normal(r, level=0.01):
    """
    Applies the Jarque-Bera test to determine if a Series is normal or not
    Test is applied at the 1% level by default
    Returns True if the hypothesis of normality is accepted, False otherwise
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(is_normal)
    else:
        statistic, p_value = scipy.stats.jarque_bera(r)
        return p_value > level

def semiDeviation(ticker):
    # Create a downside return column with the negative returns only
    
    data = returns.MonthlyNetReturn(ticker)
    downside_returns = data.loc[data < 0]

    # Calculate expected return and std dev of downside
    expected_return = data.mean()
    down_stdev = downside_returns.std()

    # Calculate the sortino ratio
    rfr = 0 #Risk free Return
    sortino_ratio = (expected_return - rfr)/down_stdev

    # Print the results
    print("Expected return  : ", expected_return*100)
    print("Downside risk   : ", down_stdev*100)
    print("Sortino ratio : ", sortino_ratio)

def maxDrawDown(ticker,startDate="2016-10-16",EndDate="2021-01-01"):# Calculate the max value 
# Calculate the max value 
    From = startDate  #'2016-10-16'
    To  = EndDate  #'2021-01-01'
    data = returns.MonthlyNetReturn(ticker)
    roll_max = data.loc[From:To,:].rolling(center=False,min_periods=1,window=250).max()
    print(roll_max)
    # Calculate the daily draw-down relative to the max
    daily_draw_down = data.loc[From:To,:]/roll_max - 1.0

    # Calculate the minimum (negative) daily draw-down
    max_daily_draw_down = daily_draw_down.rolling(center=False,min_periods=1,window=250).min()

    date =  pd.date_range("2016-10-16", periods=1060, freq="D")
    print(date)
    # Plot the results
    plt.figure(figsize=(15,15))
    plt.plot(date, daily_draw_down, label='Daily drawdown')
    plt.plot(date, max_daily_draw_down, label='Maximum daily drawdown in time-window')
    plt.legend()
    plt.show()

def var_historic(r, level=5):
    """
    Returns the historic Value at Risk at a specified level
    i.e. returns the number such that "level" percent of the returns
    fall below that number, and the (100-level) percent are above
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError("Expected r to be a Series or DataFrame")


def cvar_historic(r, level=5):
    """
    Computes the Conditional VaR of Series or DataFrame
    """
    if isinstance(r, pd.Series):
        is_beyond = r <= -var_historic(r, level=level)
        return -r[is_beyond].mean()
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TypeError("Expected r to be a Series or DataFrame")

semiDeviation("aapl")