import streamlit as st
import yfinance as yf
import pandas as pd

TICKERS = pd.read_csv('tickers.csv', header=None)
TICKERS.columns = ['symbol']

st.write('''
# Simple Stock Price App
Shown are the stock **closing** price and **volume**
         ''')
tickerSymbol = st.selectbox('Enter symbol', [i for i in TICKERS.symbol])
ticker_data = yf.Ticker(tickerSymbol)

start = st.date_input('Enter Start Date')
end = st.date_input('Enter End Date')
ticker_df = ticker_data.history(start=start, end=end)

tk = ticker_df.reset_index()
tk['Date'] = pd.to_datetime(tk['Date']).dt.strftime('%Y-%m-%d')

st.write(tk)

st.write('### Closing Price')
st.line_chart(ticker_df.Close)

st.write('### Volume Price')
st.line_chart(ticker_df.Volume)
