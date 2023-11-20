from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import author

def create_author(author: author.AuthorCreate):
    db = SessionLocal()
    return author.create_author(db, author)

def get_authors():
    db = SessionLocal()
    return author.get_authors(db)
