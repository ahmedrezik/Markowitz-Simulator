import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import datetime 

def eff_Frontier(numOfProtfolios):
    apple = pd.DataFrame(yf.download("AAPL", start="2010-01-01", end="2021-01-01")) #pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/aaple.csv', sep=',',header=None)
    amazon = pd.DataFrame(yf.download("amzn", start="2010-01-01", end="2021-01-01")) #pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/amzn.csv', sep=',',header=None)
    ford = pd.DataFrame(yf.download("f", start="2010-01-01", end="2021-01-01")) #pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/ford.csv', sep=',',header=None)
    netflix = pd.DataFrame(yf.download("nflx", start="2010-01-01", end="2021-01-01"))  #pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/nflx.csv', sep=',',header=None)
    stocks = pd.concat([apple['Close'],amazon['Close'],ford['Close'],netflix['Close']], axis=1)
    stocks.columns = ['aapl',"amzn",'ford','nflx']
    np.random.seed(42)
    num_ports = numOfProtfolios
    log_ret = np.log(stocks/stocks.shift(1))
    
    all_weights = np.zeros((num_ports, len(stocks.columns)))
    ret_arr = np.zeros(num_ports)
    vol_arr = np.zeros(num_ports)
    sharpe_arr = np.zeros(num_ports)

    for x in range(num_ports):
        # Weights
        weights = np.array(np.random.random(4))
        weights = weights/np.sum(weights)
        
        # Save weights
        all_weights[x,:] = weights
        
        # Expected return
        ret_arr[x] = np.sum( (log_ret.mean() * weights * 252))
        
        # Expected volatility
        cov_matrix = log_ret.cov()
        vol_arr[x] = np.sqrt(np.dot(weights.T, np.dot(cov_matrix*252, weights)))
        
        # Sharpe Ratio
        sharpe_arr[x] = ret_arr[x]/vol_arr[x]

    plt.figure(figsize=(12,8))
    plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    max_sr_ret = ret_arr[sharpe_arr.argmax()]
    max_sr_vol = vol_arr[sharpe_arr.argmax()]
    plt.scatter(max_sr_vol, max_sr_ret,c='red', s=50) # red dot
    plt.show()


def get_ret_vol_sr(weights):
    weights = np.array(weights)
    ret = np.sum(log_ret.mean() * weights) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
    sr = ret/vol
    return np.array([ret, vol, sr])

def neg_sharpe(weights):
# the number 2 is the sharpe ratio index from the get_ret_vol_sr
    return get_ret_vol_sr(weights)[2] * -1

def check_sum(weights):
    #return 0 if sum of the weights is 1
    return np.sum(weights)-1

eff_Frontier(6000)