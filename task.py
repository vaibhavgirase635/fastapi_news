from celery import Celery
from database import SessionLocal
from models import News
from news_fetcher import fetch_news

celery_app = Celery(
    "task", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)

@celery_app.task
def fetch_and_store_news():
    
    news_data = fetch_news()
    return news_data

celery_app.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "task.fetch_and_store_news",
        "schedule": 60.0,
    },
}
celery_app.conf.timezone = "UTC"
celery_app.conf.worker_pool = "eventlet"