# filename: stock_performance_plot.py

import matplotlib.pyplot as plt
import yfinance as yf
import datetime

# Stock data
stocks = {
    "NVIDIA (NVDA)": {
        "current_price": 119.37,
        "price_one_month_ago": 109.21,
        "percentage_change": 9.30
    },
    "Tesla (TSLA)": {
        "current_price": 214.11,
        "price_one_month_ago": 216.86,
        "percentage_change": -1.27
    }
}

# Fetch NASDAQ index data
nasdaq_ticker = "^IXIC"
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=30)
nasdaq_data = yf.download(nasdaq_ticker, start=start_date, end=end_date)

# Calculate NASDAQ percentage change
nasdaq_start_price = nasdaq_data['Close'].iloc[0]
nasdaq_end_price = nasdaq_data['Close'].iloc[-1]
nasdaq_percentage_change = ((nasdaq_end_price - nasdaq_start_price) / nasdaq_start_price) * 100

# Prepare data for plotting
labels = list(stocks.keys()) + ["NASDAQ Index"]
percentage_changes = [stocks[stock]["percentage_change"] for stock in stocks] + [nasdaq_percentage_change]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(labels, percentage_changes, color=['blue', 'green', 'red'])
plt.xlabel('Stocks/Index')
plt.ylabel('Percentage Change')
plt.title('Performance of Stocks Against NASDAQ Index Over the Past Month')
plt.ylim(min(percentage_changes) - 5, max(percentage_changes) + 5)
plt.grid(axis='y')

# Show plot
plt.show()