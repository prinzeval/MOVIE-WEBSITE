# from pydantic import BaseModel

# class EpisodeBase(BaseModel):
#     movie_id: int
#     video_link: str

# class Episode(EpisodeBase):
#     id: int

#     class Config:
#         from_attributes = True

# class MovieBase(BaseModel):
#     title: str
#     genres: str
#     country: str = None
#     duration: str = None
#     movie_year: int = None
#     description: str = None
#     jpg: str = None
#     director: str = None
#     actors: str = None

# class Movie(MovieBase):
#     id: int
#     episodes: list[Episode] = []

#     class Config:
#         from_attributes = True

# schemas.py

# schemas.py

from pydantic import BaseModel
from typing import Optional

class MovieDetailsSchema(BaseModel):
    movie_title: str
    movie_link: Optional[str] = None
    genres: Optional[str] = None
    country: Optional[str] = None
    duration: Optional[str] = None
    movie_year: Optional[int] = None  # Changed to int for consistency
    description: Optional[str] = None
    movie_image: Optional[str] = None
    director: Optional[str] = None
    actors: Optional[str] = None
    episode_links: Optional[str] = None  # Could also be a list if needed

    class Config:
        orm_mode = True
