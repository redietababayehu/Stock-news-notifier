STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import requests
stock_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=HBBFQTT24RPCS2I2"
retrieve1 = requests.get(stock_url)
data1 = retrieve1.json()
print(data1)

#Todays stock price
day2 = float(data1["Time Series (Daily)"]["2023-12-29"]["4. close"])

#yesterdays stock price
day1 = float(data1["Time Series (Daily)"]["2023-12-28"]["4. close"])

#find difference
difference = day1 - day2

#find percentage difference 
percentage_difference = (difference/day1)* 100

#create condition
#if percentage_difference > 5:
  
news_url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-29&sortBy=publishedAt&apiKey=ecf0f7a04fc243d08596474328a87997"
retrieve2 = requests.get(news_url)
data2 = retrieve2.json()
#print(data2)
news = data2['articles'][0]['title']
print(news, len(data2['articles']))





