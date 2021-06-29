from flask import Flask
from datetime import datetime
from flask import request, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://urxfhnmuzgyqzq:c1f5d1ecb1d600ab6cb310a75b828b2beca83f5d1b34e8f011a4997966a0313e@ec2-54-155-22-153.eu-west-1.compute.amazonaws.com:5432/d9focor146i5j9'

db = SQLAlchemy(app)

tickers = eval(input("\x1b[1;32m Enter the underlying stock trading ticker separated by whiteSpace \n \n some famous tickers: \n Google: GOOGL \t Apple: AAPL \n Tesla: TSLA \t Amazon: AMZN\n Netflix: nflx \t Ford Motors: F \n"))
stockData = {}
for ticker in tickers.split():
    stockData[ticker] =(pd.DataFrame(yf.download(ticker, start="1999-01-01", end="2021-01-01")))

@app.route("/")
def home():
    return "Welcome to 9090 Backend"

@app.route("/getData",methods=['GET'])
def getData():
    requestBody = request.get_json(force=True)
    ticker = requestBody['tkr']
    

