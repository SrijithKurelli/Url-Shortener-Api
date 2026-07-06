from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import Base,engine
from app.models.url import Url
from app.api.url_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to URL Shortener API"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "status": "Database Connected"
        }
    except Exception as e:
        return {
            "status": "Database Connection Failed",
            "error": str(e)
        }

app.include_router(router)
