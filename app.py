{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, jsonify\
import yfinance as yf\
\
app = Flask(__name__)\
\
@app.route('/api/stock/<ticker>', methods=['GET'])\
def get_stock_data(ticker):\
    data = yf.download(ticker, period='1d', interval='5m')\
    return data.tail(50).to_json()\
\
if __name__ == '__main__':\
    app.run()\
}