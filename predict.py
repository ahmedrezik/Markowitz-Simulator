import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
df = pd.read_csv("amzn.csv")

df = df[["Date","Adj Close"]] 
df = df.rename(columns = {"Date":"ds","Adj Close":"y"}) 
dfold = df[0:len(df)-1]


fbp = Prophet(daily_seasonality = True) 
 
fbp.fit(dfold)

fut = fbp.make_future_dataframe(periods=1) 
forecast = fbp.predict(fut)
print(forecast.tail(1))
print(df.tail(1))
#forecast = pd.read_csv("/Users/ahmed/Desktop/Bachelor/Markowitz-Simulator/forecast.csv")



# plt.figure(figsize=[8,4])
# plt.grid(True)
# plt.plot(forecast['ds'][len(forecast)-30:len(forecast)],forecast['yhat'][len(forecast)-30:len(forecast)],label='Predicted')
# plt.plot(forecast['ds'][len(forecast)-30:len(forecast)],df['y'][len(forecast)-30:len(forecast)],label='Actual')
# plt.legend(loc=True)
# plt.show()
