import pandas as pd
import numpy as numpy
import matplotlib.pyplot as  plt 
import yfinance as yf

apple =  pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/aaple.csv', sep=',',skiprows = 0)
apple.set_index('Date',inplace=True, drop=True)
print(apple[apple.index=='2020-12-18'])

apple['SMA_3'] = apple['Adj Close'].rolling(window=3).mean()
print(apple)
plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(apple['Adj Close'])
plt.plot(apple['SMA_3'],label='SMA 3 days')

plt.legend(loc=True)
plt.show()