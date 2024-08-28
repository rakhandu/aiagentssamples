# filename: icici_stock_analysis.py

import yfinance as yf

# Fetching the stock data for ICICI Bank
icici = yf.Ticker("ICICIBANK.NS")

# Getting the historical market data
hist = icici.history(period="1y")

# Getting the latest stock price
latest_price = hist['Close'][-1]

# Getting the key financial metrics
financials = icici.financials
balance_sheet = icici.balance_sheet
cashflow = icici.cashflow

# Printing the required information
print("Latest Stock Price: ", latest_price)
print("\nFinancials:\n", financials)
print("\nBalance Sheet:\n", balance_sheet)
print("\nCash Flow:\n", cashflow)