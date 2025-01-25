from fastapi import FastAPI
from database import engine, Base
from models import News


from redbeat import RedBeatSchedulerEntry
from redbeat.schedules import rrule

app = FastAPI()

@app.get("/")
def read_root():
    
    
    return {"message": "Welcome to the News API"}
