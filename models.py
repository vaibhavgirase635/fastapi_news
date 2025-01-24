from sqlalchemy import Column, Integer, String, Text
from database import Base, engine

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    description = Column(Text)
    url = Column(Text)


Base.metadata.create_all(bind=engine)