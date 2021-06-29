import requests
import json
import pandas as pd 
from pandas import json_normalize

url = ('https://newsapi.org/v2/everything?'
       'q=Amazon&'
       'from=2021-06-01&'
       'sortBy=popularity&'
       'apiKey=708b137c3fc0431ead66bd6808ebb216')

response = requests.get(url)
print(response.json())
articles = response.json()['articles']
df = json_normalize(articles)
print (df)