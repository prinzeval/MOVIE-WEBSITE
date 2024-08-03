# from sqlalchemy.orm import Session
# from sqlalchemy import or_

# import models

# def get_movies(db: Session):
#     return db.query(models.Movie).all()

# def get_movie(db: Session, movie_id: int):
#     return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

# def get_episodes(db: Session, movie_id: int):
#     return db.query(models.Episode).filter(models.Episode.movie_id == movie_id).all()

# def get_anime(db: Session):
#     genres = ['Action', 'Adventure', 'Animation']
#     genre_filters = or_(*[models.Movie.genres.like(f'%{genre}%') for genre in genres])
#     return db.query(models.Movie).filter(models.Movie.country == ' Japan').filter(genre_filters).all() #correct something valentine the space in front of the country 

# def get_asian_dramas(db : Session):
#     genres = ['Action','Romance','Comedy','Drama']
#     genre_filters = or_(*[models.Movie.genres.like(f'%{genre}%') for genre in genres])
#     return db.query(models.Movie).filter(models.Movie.country == 'South Korean').filter(genre_filters).all()

# def get_cartoon_dramas(db : Session):
#     genres = ['Animation','Comedy']
#     genre_filters = or_(*[models.Movie.genres.like(f'%{genre}%') for genre in genres])
#     return db.query(models.Movie).filter(models.Movie.country == 'United States').filter(genre_filters).all()

# def get_tv_series(db : Session):
#     genres = ['Action','Comedy','Crime','Drama','Romance']
#     genre_filters = or_(*[models.Movie.genres.like(f'%{genre}%') for genre in genres])
#     country_filters = or_(models.Movie.country == 'United States', models.Movie.country == 'United Kingdom')
#     return db.query(models.Movie).filter(country_filters).filter(genre_filters).all()



# crud.py

from sqlalchemy.orm import Session
from models import Movie
from schemas import MovieDetailsSchema
from sqlalchemy import or_

def get_all_movie_details(db: Session):
    return db.query(Movie).all()

def get_anime(db: Session):
    genres = ['Action', 'Adventure', 'Animation']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    return db.query(Movie).filter(Movie.country == 'Japan').filter(genre_filters).all()

def get_asian_dramas(db: Session):
    genres = ['Action', 'Romance', 'Comedy', 'Drama']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    return db.query(Movie).filter(Movie.country == 'South Korea').filter(genre_filters).all()

def get_cartoon_dramas(db: Session):
    genres = ['Animation', 'Comedy']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    return db.query(Movie).filter(Movie.country == 'United States').filter(genre_filters).all()

def get_tv_series(db: Session):
    genres = ['Action', 'Comedy', 'Crime', 'Drama', 'Romance']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    country_filters = or_(Movie.country == 'United States', Movie.country == 'United Kingdom')
    episode_filter = Movie.episode_links.isnot(None)
    return db.query(Movie).filter(country_filters).filter(genre_filters).filter(episode_filter).all()

def get_latest_movies(db: Session):
    genres = ['Action', 'Comedy', 'Crime', 'Drama', 'Romance']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    country_filters = or_(Movie.country == 'United States', Movie.country == 'United Kingdom')
    
    # Adjust the year for current/latest year
    return db.query(Movie).filter(
        country_filters,
        genre_filters,
        Movie.movie_year == 2024
    ).all()

def search_movies_by_name(db: Session, search_query: str):
    return db.query(Movie).filter(Movie.movie_title.ilike(f'%{search_query}%')).all()

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.movie_id == movie_id).first()
