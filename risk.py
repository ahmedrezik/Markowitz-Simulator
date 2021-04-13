import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "AAPL"
tkr = yf.Ticker(ticker)
data = pd.DataFrame(tkr.history(period="max")) 

def mean_sigma():
	stock_data = pd.DataFrame(data['Close'], columns=["Close"])
	stock_data["log"] = np.log(stock_data)-np.log(stock_data.shift(1))
	st = stock_data["log"].dropna().ewm(span=252).std()
	sigma = st.iloc[-1]
	return sigma
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




volatilty()
print(mean_sigma())    