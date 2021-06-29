import numpy as np
import pandas as pd
from urllib.parse import urlencode
#from pandas_datareader import data as wb
import yfinance as yf
import matplotlib.pyplot as plt
import re
import os

ticker = eval(input("\x1b[1;32m Enter the underlying stock trading ticker separated by whiteSpace \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))

stockData =pd.DataFrame(yf.download(ticker, start="1999-01-01", end="2021-01-01"))
stockData.to_csv(f'/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/{ticker}.csv', index = True)
