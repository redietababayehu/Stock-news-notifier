import send_SMS
import requests
import config

# a function that finds the date 
def get_stock_info(ticker: str, date: str):
    stock_url = f"https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={config.api_key_stock}"
    response = requests.get(stock_url)
    json = response.json()
    return json

#Todays stock price
day2 = float(get_stock_info('TSLA','2023-12-28')["close"])
#yesterdays stock price
day1 = float(get_stock_info('TSLA','2023-12-27')["close"])

#find difference
difference = day1 - day2

#find percentage difference 
percentage_difference = (difference/day1)* 100


#function to get data specifications from the user
def get_news(company_name: str, date: str):
    news_url = f"https://newsapi.org/v2/top-headlines?q={company_name}&from={date}&sortBy=publishedAt&apiKey={config.api_key_news}"
    response = requests.get(news_url)
    json = response.json()
    return json

articles = []

#use a for loop to append te first 3 articles
for i in range(3):
    title = str(get_news('tesla','2023-12-28')['articles'][i]['title'])
    description = str(get_news('tesla','2023-12-28')['articles'][i]['description'])
    news = title + ': ' + description
    articles.append(news)
    
if percentage_difference > 1:
    for article in articles:
        send_SMS.create_message(article, +18436281404, +17788876392)



