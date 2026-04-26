
import os

from newsapi import NewsApiClient
from newspaper import Article

news_api_key=os.getenv("NEWS_API_KEY")

def get_newapi_client():
    return NewsApiClient(api_key=news_api_key)

def fetch_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        
        return article.text
    except Exception as e:
        return None

