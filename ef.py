import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime 
import scipy
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import minimize
# ! Generize the number of input stocks
def eff_Frontier():
    # apple =  pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/aaple.csv', sep=',',skiprows = 0)
    # apple.set_index('Date',inplace=True, drop=True)
    # amazon = pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/amzn.csv', sep=',',skiprows = 0)
    # ford = pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/ford.csv', sep=',',skiprows = 0)
    # netflix = pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/nflx.csv', sep=',',skiprows = 0)
   
    stocks = pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/stocks.csv', sep=',',skiprows = 0)
    stocks.set_index('Date',inplace=True, drop=True)
    print(stocks)
    #stocks.columns = ['aapl',"amzn",'nflx','ford']
    print(stocks.iloc[0])
    # Normalize Stock Prices
    df3 = stocks.divide(stocks.iloc[0] / 100)
    plt.figure(figsize=(15, 6))
    for i in range(df3.shape[1]):
        plt.plot(df3.iloc[:,i], label=df3.columns.values[i])
    plt.legend(loc='upper left', fontsize=12)
    plt.ylabel('Normalized prices')
    plt.show()
    #Calculate daily changes in the stocks' value
    returns = stocks.pct_change()
    #Remove nan values at the first row of df2. Create a new dataframe df
    df=returns.iloc[1:len(stocks.index),:]
    # Calculate annualized average return for each stock. Annualized average return = Daily average return * 252 business days.
    annualized_r = np.mean(df,axis=0)*252
    covar = df3.cov()
    
    bounds = Bounds(0,1)
    linear_constraint = LinearConstraint(np.ones((stocks.shape[1],), dtype=int),1,1)
    
    
    #Create x0, the first guess at the values of each stock's weight.
    weights = np.ones(stocks.shape[1])
    x0 = weights/np.sum(weights)
    #Define a function to calculate volatility
    fun1 = lambda w: np.sqrt(np.dot(w,np.dot(w,covar)))
    res = minimize(fun1,x0,method='trust-constr',constraints = linear_constraint,bounds = bounds)

    #These are the weights of the stocks in the portfolio with the lowest level of risk possible.
    w_min = res.x

    np.set_printoptions(suppress = True, precision=2)
    print(w_min)
    print("Minimum Risk: " 'return: % .2f'% (ret(annualized_r,w_min)*100), 'risk: % .3f'% vol(w_min,covar))

    fun2 = lambda w: np.sqrt(np.dot(w,np.dot(w,covar)))/annualized_r.dot(w)
    res_sharpe = minimize(fun2,x0,method='trust-constr',constraints = linear_constraint,bounds = bounds)

    #These are the weights of the stocks in the portfolio with the highest Sharpe ratio.
    w_sharpe = res_sharpe.x
    print(w_sharpe)
    print("Best Sharpe:" 'return: % .2f'% (ret(annualized_r,w_sharpe)*100), 'risk: % .3f'% vol(w_sharpe,covar))
    w = w_min
    num_ports = 100
    gap = (np.amax(annualized_r) - ret(annualized_r,w_min))/num_ports


    all_weights = np.zeros((num_ports, len(df.columns)))
    all_weights[0],all_weights[1]=w_min,w_sharpe
    ret_arr = np.zeros(num_ports)
    ret_arr[0],ret_arr[1]=ret(annualized_r,w_min),ret(annualized_r,w_sharpe)
    vol_arr = np.zeros(num_ports)
    vol_arr[0],vol_arr[1]=vol(w_min,covar),vol(w_sharpe,covar)

    for i in range(num_ports):
        port_ret = ret(annualized_r,w) + i*gap
        double_constraint = LinearConstraint([np.ones(stocks.shape[1]),annualized_r],[1,port_ret],[1,port_ret])
        
        #Create x0: initial guesses for weights.
        x0 = w_min
        #Define a function for portfolio volatility.
        fun = lambda w: np.sqrt(np.dot(w,np.dot(w,covar)))
        a = minimize(fun,x0,method='trust-constr',constraints = double_constraint,bounds = bounds)
        
        all_weights[i,:]=a.x
        ret_arr[i]=port_ret
        vol_arr[i]=vol(a.x,covar)
        
    sharpe_arr = ret_arr/vol_arr  

    plt.figure(figsize=(20,10))
    plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.show()

def ret(r,w):
    return r.dot(w)
# Risk level - or volatility
def vol(w,covar):
    return np.sqrt(np.dot(w,np.dot(w,covar)))
def sharpe (ret,vol):
    return ret/vol



eff_Frontier()