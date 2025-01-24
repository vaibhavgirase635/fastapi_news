import requests, json
from database import SessionLocal
from models import News

NEWS_API_URL = "https://newsapi.org/v2/everything?q=cricket&apiKey=63c0d4a0ec9840fe92fee1984163ce9e"
API_KEY = "63c0d4a0ec9840fe92fee1984163ce9e"

def fetch_news():
    response = requests.get(NEWS_API_URL)
    news_data = response.json()["articles"]
    # print(news_data)
    session = SessionLocal()
    news = []
    for article in news_data:
        news.append(article["title"])
        news_item = News(
            title=article["title"],
            description=article["description"],
            url=article["url"],
        )
        session.add(news_item)
    
    session.commit()
    session.close()
    print(news)
    return news
    
