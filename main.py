from fastapi import FastAPI, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, schemas
from database import SessionLocal, engine
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response
from uuid import UUID
import uvicorn  
import models

# Create database tables (only for initial setup, avoid running this on every start in production)
models.Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template directory
templates = Jinja2Templates(directory="templates")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def get_all_movie_details(request: Request, db: Session = Depends(get_db)):
    # Fetch different categories of movies
    anime_movies = crud.get_anime(db)
    asian_dramas = crud.get_asian_dramas(db)
    cartoons = crud.get_cartoon_dramas(db)
    tv_series = crud.get_tv_series(db)
    latest_movies = crud.get_latest_movies(db)
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "anime_movies": anime_movies,
        "asian_dramas": asian_dramas,
        "cartoons": cartoons,
        "tv_series": tv_series,
        "latest_movies": latest_movies,
        "search_results": [], # Initialize the search_results as an empty list 
        "featured_movies": latest_movies
    })

@app.get("/search-movies/", response_class=HTMLResponse)
def search_movies_by_name_endpoint(request: Request, search_query: str, db: Session = Depends(get_db)):
    # Fetch search results
    search_results = crud.search_movies_by_name(db, search_query)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "anime_movies": [],
        "asian_dramas": [],
        "cartoons": [],
        "tv_series": [],
        "latest_movies": [],
        "search_results": search_results
    })

@app.get("/specific-anime/", response_model=List[schemas.MovieDetailsSchema])
def read_anime_movies(db: Session = Depends(get_db)):
    movies = crud.get_anime(db)
    return movies

@app.get("/specific-asian/", response_model=List[schemas.MovieDetailsSchema])
def read_asian_movie(db: Session = Depends(get_db)):
    movies = crud.get_asian_dramas(db)
    return movies

@app.get("/specific-cartoon/", response_model=List[schemas.MovieDetailsSchema])
def read_cartoons(db: Session = Depends(get_db)):
    movies = crud.get_cartoon_dramas(db)
    return movies

@app.get("/specific-tvseries/", response_model=List[schemas.MovieDetailsSchema])
def read_tv_series(db: Session = Depends(get_db)):
    movies = crud.get_tv_series(db)
    return movies

@app.get("/specific-latest-movie/", response_model=List[schemas.MovieDetailsSchema])
def read_latest_movies(db: Session = Depends(get_db)):
    movies = crud.get_latest_movies(db)
    return movies

@app.get("/watch/{movie_id}", response_class=HTMLResponse)
def watch_movie(movie_id: UUID, request: Request, db: Session = Depends(get_db)):
    movie = crud.get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return templates.TemplateResponse("src.html", {"request": request, "movie": movie})

@app.get("/favicon.ico")
async def favicon(request: Request):
    return Response(status_code=204)  # No Content

# Run the app with Uvicorn if this file is run directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
