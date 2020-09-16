from flask import Flask
import pandas_datareader as pdr
from datetime import date

app = Flask(__name__)

today = date.today()
now   = today.strftime("%Y-%m-%d")

@app.route('/', defaults={'Code': '005930.KS', 'From': '2020-01-01', 'To':now})
@app.route('/<code>', methods=['GET'])
def getCode (Code, From, To):
    df = pdr.DataReader('005930.KS', 'yahoo', From, To)
    return df.to_json(None, "index")
