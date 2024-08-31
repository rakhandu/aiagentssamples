# filename: stock_news_insights.py

import requests

def get_news_insights(stock_symbol, api_key):
    url = f"https://api.bing.microsoft.com/v7.0/news/search?q={stock_symbol}&count=5"
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }
    response = requests.get(url, headers=headers)
    
    # Debugging: Print the request URL, headers, response status, and the first few lines of the response data
    print(f"Request URL: {url}")
    print(f"Request Headers: {headers}")
    print(f"Response Status: {response.status_code}")
    print(f"Response Data: {response.text[:500]}")  # Print the first 500 characters of the response
    
    data = response.json()
    
    if response.status_code == 200:
        articles = data['value']
        news_insights = []
        
        for article in articles:  # Get top 5 news articles
            headline = article['name']
            summary = article['description']
            news_insights.append({'headline': headline, 'summary': summary})
        
        return news_insights
    else:
        return []

def main():
    api_key = 'YOUR_BING_API_KEY'  # Replace with your Bing News Search API key
    stocks = ['NVDA', 'TSLA']
    for stock in stocks:
        print(f"Top news insights for {stock}:")
        news_insights = get_news_insights(stock, api_key)
        for i, news in enumerate(news_insights, 1):
            print(f"{i}. {news['headline']}")
            print(f"   {news['summary']}\n")

if __name__ == "__main__":
    main()