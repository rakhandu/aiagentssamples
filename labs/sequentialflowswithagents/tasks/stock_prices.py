# filename: stock_prices.py

import yfinance as yf
from datetime import datetime, timedelta

# Define the stock tickers
tickers = ['NVDA', 'TSLA']

# Get today's date and the date one month ago
today = datetime.today().date()
one_month_ago = today - timedelta(days=30)

# Function to get stock data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(start=one_month_ago, end=today)
    return hist

# Function to calculate percentage change
def calculate_percentage_change(start_price, end_price):
    return ((end_price - start_price) / start_price) * 100

# Fetch data and calculate percentage change for each ticker
for ticker in tickers:
    data = get_stock_data(ticker)
    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]
    percentage_change = calculate_percentage_change(start_price, end_price)
    print(f"Ticker: {ticker}")
    print(f"Current Price: {end_price:.2f}")
    print(f"Price One Month Ago: {start_price:.2f}")
    print(f"Percentage Change Over the Past Month: {percentage_change:.2f}%\n")