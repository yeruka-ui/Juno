from .command_helper import newJson
import requests
import os

def get_news(command, confidence, topic = 'General'):
   API_KEY = os.getenv('NEWS_API_KEY')
   url = f"https://gnews.io/api/v4/top-headlines?category={topic}&lang=en&max=5&apikey={API_KEY}"

   response = requests.get(url)
   news_json = response.json()
   news_articles = news_json['articles']

   articles = []
   #iterate to news_json
   for news in news_articles:
       articles.append({
           "title": news['title'],
           "url": news['url'],
           "content": news['content'],
           "date": news['publishedAt'],
           "imageUrl": news['image'],
       })
   return newJson(command, confidence, articles)




