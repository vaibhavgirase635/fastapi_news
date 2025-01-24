from sqlalchemy import Column, Integer, String, Text
from database import Base, engine

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    url = Column(String(255))


Base.metadata.create_all(bind=engine)