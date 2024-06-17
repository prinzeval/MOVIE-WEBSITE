# from sqlalchemy import Boolean, Column, Integer , String ,ForeignKey
# from database import Base

# class Todo(Base):
#     __tablename__ = "todos"
    
#     id = Column(Integer, primary_key = True, index = True)
#     title = Column(String)
#     complete = Column(Boolean, default = False) 



from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Movie(Base):
    __tablename__ = "Movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    genres = Column(String(255), nullable=False)
    country = Column(String(100))
    duration = Column(String(100))
    movie_year = Column(Integer)
    description = Column(String)
    jpg = Column(String(255))
    director = Column(String(255))
    actors = Column(String(255))

    episodes = relationship("Episode", back_populates="movie")

class Episode(Base):
    __tablename__ = "Episodes"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("Movies.id"))
    video_link = Column(String(255))

    movie = relationship("Movie", back_populates="episodes")

