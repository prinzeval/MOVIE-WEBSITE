from uuid import UUID
from sqlalchemy.orm import Session
from models import Movie
from sqlalchemy import or_, and_
from typing import List, Optional

def get_all_movie_details(db: Session):
    """
    Retrieve all movie details from the database.
    """
    return db.query(Movie).all()

def get_anime(db: Session):
    """
    Retrieve anime movies from Japan that belong to specific genres.
    """
    genres = ['Action', 'Adventure', 'Animation']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    return db.query(Movie).filter(Movie.country == 'Japan').filter(genre_filters).all()

def get_asian_dramas(db: Session):
    """
    Retrieve Asian dramas (from South Korea) that belong to specific genres.
    """
    genres = ['Action', 'Romance', 'Comedy', 'Drama']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    return db.query(Movie).filter(Movie.country == 'South Korea').filter(genre_filters).all()

def get_cartoon_dramas(db: Session):
    """
    Retrieve cartoon dramas from the United States that belong to Animation and Comedy genres.
    """
    genre_filters = and_(
        Movie.genres.like('%Animation%'),
        Movie.genres.like('%Comedy%')
    )
    return db.query(Movie).filter(Movie.country == 'United States').filter(genre_filters).all()

def get_tv_series(db: Session):
    """
    Retrieve TV series from the United States and United Kingdom that belong to specific genres and have episode links.
    """
    genres = ['Action', 'Comedy', 'Crime', 'Drama', 'Romance']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    country_filters = or_(Movie.country == 'United States', Movie.country == 'United Kingdom')
    episode_filter = Movie.episode_links.isnot(None)
    return db.query(Movie).filter(country_filters).filter(genre_filters).filter(episode_filter).all()

def get_latest_movies(db: Session):
    """
    Retrieve the latest movies (from the year 2024) from the United States and United Kingdom that belong to specific genres.
    """
    genres = ['Action', 'Comedy', 'Crime', 'Drama', 'Romance']
    genre_filters = or_(*[Movie.genres.like(f'%{genre}%') for genre in genres])
    country_filters = or_(Movie.country == 'United States', Movie.country == 'United Kingdom')
    
    return db.query(Movie).filter(
        country_filters,
        genre_filters,
        Movie.movie_year == '2024'  # Keep movie_year as a string
    ).all()

def search_movies_by_name(db: Session, search_query: str):
    """
    Search movies by their title.
    """
    return db.query(Movie).filter(Movie.movie_title.ilike(f'%{search_query}%')).all()

def get_movie_by_id(db: Session, movie_id: UUID) -> Optional[Movie]:
    """
    Retrieve a movie by its ID.
    """
    return db.query(Movie).filter(Movie.movie_id == movie_id).first()
