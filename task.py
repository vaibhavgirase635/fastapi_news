from celery import Celery
from database import SessionLocal
from models import News
from news_fetcher import fetch_news
from celery.schedules import crontab
import requests, os

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_URL = f"https://newsapi.org/v2/everything?q=cricket&apiKey={NEWS_API_KEY}"

celery_app = Celery(
    "task", broker="redis://localhost:6379/0"
)

@celery_app.task
def fetch_news():
    try:
        # Fetch news from the API
        response = requests.get(NEWS_API_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        news_data = response.json().get("articles", [])

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
        
        print(f"Fetched {len(news_data)} articles")
        return [article["title"] for article in news_data]

    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


    

celery_app.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "task.fetch_news",
        'schedule': crontab(minute='*/1'),  # Every minute
    },
}
celery_app.conf.timezone = "UTC"

celery_app.conf.broker_connection_retry_on_startup = True
