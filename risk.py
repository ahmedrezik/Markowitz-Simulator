import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import datetime 
#! Modularize The code 
ticker = "AAPL"#eval(input("\x1b[1;32m Enter the underlying stock trading ticker \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))
tkr = yf.Ticker(ticker)
data = pd.DataFrame(yf.download(ticker, start="1999-01-01", end="2021-01-01"))  

def mean_sigma():
	stock_data = pd.DataFrame(data['Close'], columns=["Close"])
	stock_data["log"] = np.log(stock_data)-np.log(stock_data.shift(1))
	st = stock_data["log"].dropna().ewm(span=252).std()
	sigma = st.iloc[-1]
	return sigma

def Sortino_Ratio(): #Donwside Risk
        # Create a downside return column with the negative returns only
        #! Why traget return is 0?
    downside_returns = data.loc[data['pf_returns'] < target]

    # Calculate expected return and std dev of downside
    expected_return = data['pf_returns'].mean()
    down_stdev = downside_returns['pf_returns'].std()

    # Calculate the sortino ratio
    rfr = 0 #Risk free Return
    sortino_ratio = (expected_return - rfr)/down_stdev

    # Print the results
    print("Expected return  : ", expected_return*100)
    print("Downside risk   : ", down_stdev*100)
    print("Sortino ratio : ", sortino_ratio)

def maxDrawDown():# Calculate the max value 
# Calculate the max value 
    From = '2016-10-16'
    To   = '2021-01-01'
    roll_max = data.loc[From:To,:]["Adj Close"].rolling(center=False,min_periods=1,window=250).max()
    print(roll_max)
    # Calculate the daily draw-down relative to the max
    daily_draw_down = data.loc[From:To,:]["Adj Close"]/roll_max - 1.0

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

#! Fix the monthly return  
def covariance():
        # Get percentage daily returns
    daily_returns = data.pct_change()

    # Assign portfolio weights
    weights = np.array([0.05, 0.4, 0.3, 0.25])

        # Calculate the covariance matrix 
    cov_matrix = (daily_returns.cov())*250
    port_variance = np.dot(weights.T, np.dot(cov_matrix, weights))

    # Print the result
    print(str(np.round(port_variance, 4) * 100) + '%')


def volatilty():
        # calculate daily logarithmic return
    data['returns'] = (np.log(data['Close'] /
        data['Close'].shift(-1)))
        
    # calculate daily standard deviation of returns
    daily_std = np.std(data.returns)
    
    # annualized daily standard deviation
    std = daily_std * 252 ** 0.5
    # Plot histograms
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    n, bins, patches = ax.hist(
        data.returns.values,
        bins=50, alpha=0.65, color='blue')
    
    ax.set_xlabel('log return of stock price')
    ax.set_ylabel('frequency of log return')
    ax.set_title('Historical Volatility for ' +
        ticker)
    
    # get x and y coordinate limits
    x_corr = ax.get_xlim()
    y_corr = ax.get_ylim()
    
    # make room for text
    header = y_corr[1] / 5
    y_corr = (y_corr[0], y_corr[1] + header)
    ax.set_ylim(y_corr[0], y_corr[1])
    
    # print historical volatility on plot
    x = x_corr[0] + (x_corr[1] - x_corr[0]) / 30
    y = y_corr[1] - (y_corr[1] - y_corr[0]) / 15
    ax.text(x, y , 'Annualized Volatility: ' + str(np.round(std*100, 1))+'%',
        fontsize=11, fontweight='bold')
    x = x_corr[0] + (x_corr[1] - x_corr[0]) / 15
    y -= (y_corr[1] - y_corr[0]) / 20
    
    # save histogram plot of historical price volatility
    fig.tight_layout()
    fig.savefig('historical volatility.png')



maxDrawDown()