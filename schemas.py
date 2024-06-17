from pydantic import BaseModel

class EpisodeBase(BaseModel):
    movie_id: int
    video_link: str

class Episode(EpisodeBase):
    id: int

    class Config:
        from_attributes = True

class MovieBase(BaseModel):
    title: str
    genres: str
    country: str = None
    duration: str = None
    movie_year: int = None
    description: str = None
    jpg: str = None
    director: str = None
    actors: str = None

class Movie(MovieBase):
    id: int
    episodes: list[Episode] = []

    class Config:
        from_attributes = True