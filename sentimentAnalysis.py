import os
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen, Request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
import json
from pandas import json_normalize

def parse():

    web_url = 'https://finviz.com/quote.ashx?t='
    crypto_url = 'https://finviz.com/crypto_charts.ashx?t='
    
    news_tables = {}
    tickers = ['AMZN', 'GOOG', 'TSLA', "AAPL"]
    #crypto = ['BTCUSD', "ETHUSD", "XRPUSD", "LTCUSD"]

    for tick in tickers:
        url = web_url + tick
        response = requests.get(url)
        req = Request(url=url,headers={"User-Agent": "Chrome"}) 
        response = urlopen(req)    
        html = BeautifulSoup(response,"html.parser")
        news_table = html.find(class_='fullview-news-outer')
        news_tables[tick] = news_table
        news_list = []


    for file_name, news_table in news_tables.items():
        for i in news_table.findAll('tr'):
            
            text = i.a.get_text() 
            
            date_scrape = i.td.text.split()

            if len(date_scrape) == 1:
                time = date_scrape[0]
                
            else:
                date = date_scrape[0]
                time = date_scrape[1]

            tick = file_name.split('_')[0]
            
            news_list.append([tick, date, time, text])
    
    vader = SentimentIntensityAnalyzer()
    columns = ['ticker', 'date', 'time', 'headline']
    news_df = pd.DataFrame(news_list, columns=columns)
    scores = news_df['headline'].apply(vader.polarity_scores).tolist()
    scores_df = pd.DataFrame(scores)

    news_df = news_df.join(scores_df, rsuffix='_right')

    news_df['date'] = pd.to_datetime(news_df.date).dt.date
    plt.rcParams['figure.figsize'] = [10, 6]

    mean_scores = news_df.groupby(['ticker','date']).mean()

    mean_scores = mean_scores.unstack()

    mean_scores = mean_scores.xs('compound', axis="columns").transpose()

    mean_scores.plot(kind = 'bar')

    plt.grid()

    plt.show()



parse()      

