# from fastapi import FastAPI, Depends, Request, Form, status

# from starlette.responses import RedirectResponse
# from starlette.templating import Jinja2Templates
# from sqlalchemy.orm import Session


# import models
# from database import engine ,SessionLocal
# models.Base.metadata.create_all(bind = engine)

# templates = Jinja2Templates(directory= "templates")

# app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()    

# @app.get("/")
# def home(request: Request, db: Session = Depends(get_db)):
#     todos = db.query(models.Todo).all()
#     return templates.TemplateResponse("index.html",
#                                       {"request": request, "todo_list": todos})

# @app.post("/add")
# def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
#     new_todo = models.Todo(title = title)
#     db.add(new_todo)
#     db.commit()

#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code = status.HTTP_303_SEE_OTHER)

# @app.get("/update/{todo_id}")
# def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
#     todo  = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     todo.complete = not todo.complete
#     db.commit()

#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code = status.HTTP_302_FOUND)

# @app.get("/delete/{todo_id}")
# def delete(request :Request, todo_id : int, db: Session = Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     db.delete(todo)
#     db.commit()
    
#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code = status.HTTP_302_FOUND)










# from fastapi import FastAPI, Depends, Request, Form, status
# from starlette.responses import RedirectResponse
# from starlette.templating import Jinja2Templates
# from sqlalchemy.orm import Session
# import models
# from database import engine, SessionLocal

# models.Base.metadata.create_all(bind=engine)

# templates = Jinja2Templates(directory="templates")

# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/")
# def home(request: Request, db: Session = Depends(get_db)):
#     todos = db.query(models.Todo).all()
#     return templates.TemplateResponse("index.html", {"request": request, "todo_list": todos})

# @app.post("/add")
# def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
#     new_todo = models.Todo(title=title)
#     db.add(new_todo)
#     db.commit()

#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

# @app.get("/update/{todo_id}")
# def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     todo.complete = not todo.complete
#     db.commit()

#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

# @app.get("/delete/{todo_id}")
# def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     db.delete(todo)
#     db.commit()
    
#     url = app.url_path_for("home")
#     return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)




# First prototype


# from fastapi import FastAPI, Depends, HTTPException, Request, status
# from fastapi.staticfiles import StaticFiles
# from sqlalchemy.orm import Session
# import models, schemas, crud, database
# from starlette.templating import Jinja2Templates

# models.Base.metadata.create_all(bind=database.engine)


# app = FastAPI()


# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")


# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/movies/", response_model=list[schemas.Movie])
# def read_movies(request: Request, db: Session = Depends(get_db)):
#     movies = crud.get_movies(db)
#     return movies
#     # return templates.TemplateResponse("index.html", {"request": request, "movies": movies})


# @app.get("/movies/{movie_id}", response_model=schemas.Movie)
# def read_movie(request: Request, movie_id: int, db: Session = Depends(get_db)):
#     db_movie = crud.get_movie(db, movie_id=movie_id)
#     if db_movie is None:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return db_movie 

# @app.get("/movies/{movie_id}/episodes/", response_model=list[schemas.Episode])
# def read_episodes(request: Request, movie_id: int, db: Session = Depends(get_db)):
#     episodes = crud.get_episodes(db, movie_id=movie_id)
#     return episodes

# @app.get("/specific-anime/", response_model=list[schemas.Movie])
# def read_anime_movies(db: Session = Depends(get_db)):
#     movies = crud.get_anime(db)
#     return movies

# @app.get("/specific-asian/",response_model=list[schemas.Movie])
# def read_asian_movie(db: Session = Depends(get_db)):
#     movies = crud.get_asian_dramas(db)
#     return movies

# @app.get("/specific-cartoon/",response_model=list[schemas.Movie])
# def read_cartoons(db : Session = Depends(get_db)):
#     movies = crud.get_cartoon_dramas(db)
#     return movies

# @app.get("/specific-tvseries/",response_model=list[schemas.Movie])
# def read_tv_series(db : Session = Depends(get_db)):
#     movies = crud.get_tv_series(db)
#     return movies











# main.py

from fastapi import FastAPI, Depends, Request, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


# Create database tables
models.Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to get all MovieDetails
@app.get("/moviedetails/", response_model=list[schemas.MovieDetailsSchema])
def get_all_movie_details(request: Request, db: Session = Depends(get_db)):
    movies = crud.get_all_movie_details(db)
    return templates.TemplateResponse("index.html", {"request": request, "movies": movies})

@app.get("/specific-anime/", response_model=list[schemas.MovieDetailsSchema])
def read_anime_movies(db: Session = Depends(get_db)):
    movies = crud.get_anime(db)
    return movies

@app.get("/specific-asian/",response_model=list[schemas.MovieDetailsSchema])
def read_asian_movie(db: Session = Depends(get_db)):
    movies = crud.get_asian_dramas(db)
    return movies

@app.get("/specific-cartoon/",response_model=list[schemas.MovieDetailsSchema])
def read_cartoons(db : Session = Depends(get_db)):
    movies = crud.get_cartoon_dramas(db)
    return movies

@app.get("/specific-tvseries/",response_model=list[schemas.MovieDetailsSchema])
def read_tv_series(db : Session = Depends(get_db)):
    movies = crud.get_tv_series(db)
    return movies


@app.get("/specific-latest-movie/",response_model=list[schemas.MovieDetailsSchema])
def read_latest_movies(db : Session = Depends(get_db)):
    movies = crud.get_latest_movies(db)
    return movies

@app.get("/search-movies/", response_model=list[schemas.MovieDetailsSchema])
def search_movies_by_name_endpoint(request: Request, search_query: str, db: Session = Depends(get_db)):
    movies = crud.search_movies_by_name(db, search_query)
    return movies

@app.get("/watch/{movie_id}", response_class=HTMLResponse)
def watch_movie(movie_id: int, request: Request, db: Session = Depends(get_db)):
    print(f"Fetching movie with ID: {movie_id}")  # Add logging
    movie = crud.get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    print(f"Movie found: {movie.movie_title}")  # Add logging 
    return templates.TemplateResponse("src.html", {"request": request, "movie": movie})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)