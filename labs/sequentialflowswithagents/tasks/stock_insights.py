# filename: stock_insights.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime
import time

def get_stock_data(stock_symbol):
    options = Options()
    options.headless = True
    service = Service(executable_path='/path/to/chromedriver')  # Update with the path to your chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    
    url = f'https://finance.yahoo.com/quote/{stock_symbol}/history?p={stock_symbol}'
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    table = soup.find('table', {'data-test': 'historical-prices'})
    
    if not table:
        raise ValueError(f"Could not find the historical prices table for {stock_symbol}")
    
    rows = table.find_all('tr')
    
    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) < 6:
            continue
        date = cols[0].text
        close_price = cols[4].text.replace(',', '')
        data.append((date, float(close_price)))
    
    return data

def calculate_percentage_change(data):
    start_price = data[-1][1]
    end_price = data[0][1]
    percentage_change = ((end_price - start_price) / start_price) * 100
    return percentage_change

def plot_stock_data(stock_symbol, data):
    dates = [datetime.strptime(d[0], '%b %d, %Y') for d in data]
    prices = [d[1] for d in data]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linestyle='-', label=stock_symbol)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'{stock_symbol} Stock Prices Over the Past Month')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    stocks = ['NVDA', 'TSLA']
    insights = {}
    
    for stock in stocks:
        try:
            data = get_stock_data(stock)
            percentage_change = calculate_percentage_change(data)
            insights[stock] = {
                'current_price': data[0][1],
                'percentage_change': percentage_change,
                'data': data
            }
        except ValueError as e:
            print(e)
            continue
    
    for stock, info in insights.items():
        print(f"**{stock}**")
        print(f"Current Price: ${info['current_price']:.2f}")
        print(f"Percentage Change Over the Past Month: {info['percentage_change']:.2f}%")
        plot_stock_data(stock, info['data'])

if __name__ == "__main__":
    main()