from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from decouple import config



DB_USER = config("DB_USER")
print(DB_USER)
DB_PASSWORD = config("DB_PASSWORD")
print(DB_PASSWORD)
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/newsdb"
# DATABASE_URL = "postgresql://postgres:vaibhav123@localhost/pizza_delivery"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

