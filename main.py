from fastapi import FastAPI
from database import engine, Base
from models import News

from news_fetcher import fetch_news
from redbeat import RedBeatSchedulerEntry
from redbeat.schedules import rrule

app = FastAPI()

@app.get("/")
def read_root():
    response = fetch_news()
    
    return {"message": "Welcome to the News API","news":response}
