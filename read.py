import numpy as np
import pandas as pd
apple =  pd.read_csv('/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/aaple.csv', sep=',',skiprows = 0)
apple.set_index('Date',inplace=True, drop=True)
print(apple)