import  numpy as np  
import pandas  as pd

prices =  pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/prices.csv', sep=',',skiprows = 0)
prices.set_index('Date',inplace=True, drop=True)
print(prices)