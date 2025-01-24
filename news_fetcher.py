import requests, json
from database import SessionLocal
from models import News

NEWS_API_URL = "https://newsapi.org/v2/everything?q=top-headlines&from=2024-12-24&sortBy=publishedAt&apiKey=63c0d4a0ec9840fe92fee1984163ce9e"
API_KEY = "63c0d4a0ec9840fe92fee1984163ce9e"

def fetch_news():
   
    

    response = requests.get(NEWS_API_URL)
    news_data = response.json()["articles"]
    print(news_data)
    session = SessionLocal()
    
    for article in news_data:
        news_item = News(
            title=article["title"],
            description=article["description"],
            url=article["url"],
        )
        session.add(news_item)
    
    session.commit()
    session.close()
    return news_data
    
