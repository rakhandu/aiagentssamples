# filename: msft_price_prediction.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

# Step 1: Download the MSFT share price data for the last 3 months
msft = yf.Ticker("MSFT")
data = msft.history(period="3mo")

# Step 2: Print the fields in the dataset
print("Fields in the dataset:")
print(data.columns)

# Prepare the data for Prophet
df = data.reset_index()[['Date', 'Close']]
df.columns = ['ds', 'y']

# Check for missing data
if df.isnull().values.any():
    df = df.dropna()

# Step 3: Use Prophet to predict the share price for the next 3 months
model = Prophet()
model.fit(df)

# Create a dataframe to hold predictions
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# Step 4: Plot the historical data and the forecasted data
plt.figure(figsize=(10, 6))
plt.plot(df['ds'], df['y'], label='Historical Data')
plt.plot(forecast['ds'], forecast['yhat'], label='Forecasted Data')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('MSFT Share Price Prediction')
plt.legend()
plt.grid(True)  # Add grid lines

# Step 5: Save the plot to a file named MSFT_price.png
plt.savefig('MSFT_price.png')
plt.show()