from fastapi import FastAPI
from database import engine, Base
from models import News
from task import fetch_and_store_news
from news_fetcher import fetch_news

app = FastAPI()

@app.get("/")
def read_root():
    response = fetch_news()
    return {"message": "Welcome to the News API","news":response}
