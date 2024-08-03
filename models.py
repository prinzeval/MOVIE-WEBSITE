# from sqlalchemy import Boolean, Column, Integer , String ,ForeignKey
# from database import Base

# class Todo(Base):
#     __tablename__ = "todos"
    
#     id = Column(Integer, primary_key = True, index = True)
#     title = Column(String)
#     complete = Column(Boolean, default = False) 


#first prototype



# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base

# class Movie(Base):
#     __tablename__ = "Movies"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(255), nullable=False)
#     genres = Column(String(255), nullable=False)
#     country = Column(String(100))
#     duration = Column(String(100))
#     movie_year = Column(Integer)
#     description = Column(String)
#     jpg = Column(String(255))
#     director = Column(String(255))
#     actors = Column(String(255))

#     episodes = relationship("Episode", back_populates="movie")

# class Episode(Base):
#     __tablename__ = "Episodes"

#     id = Column(Integer, primary_key=True, index=True)
#     movie_id = Column(Integer, ForeignKey("Movies.id"))
#     video_link = Column(String(255))

#     movie = relationship("Movie", back_populates="episodes")


# models.py

from sqlalchemy import Column, Integer, String, Text
from database import Base

class Movie(Base):
    __tablename__ = 'movies'
    
    movie_id = Column(Integer, primary_key=True, index=True)
    movie_title = Column(String, index=True)
    movie_image = Column(String, nullable=True)
    genres = Column(String, nullable=True)
    country = Column(String, nullable=True)
    director = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    movie_year = Column(Integer, nullable=True)
    actors = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    movie_link = Column(String, nullable=True)
    episode_links = Column(Text, nullable=True)  # Assuming episode_links is a list of URLs stored as a JSON or Text
