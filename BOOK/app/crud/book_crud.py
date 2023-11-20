from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import book

def get_books(title_startswith: str = None, author_id: int = None):
    db = SessionLocal()
    return book.get_books(db, title_startswith=title_startswith, author_id=author_id)

def create_book(book: book.BookCreate):
    db = SessionLocal()
    return book.create_book(db, book)

def get_client_books(client_id: int):
    db = SessionLocal()
    return book.get_client_books(db, client_id=client_id)
