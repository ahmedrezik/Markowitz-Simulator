import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

gme = yf.Ticker("GME")
data = pd.DataFrame(gme.history(period="max"))
print(data["Close"]["2021-03-16"])
