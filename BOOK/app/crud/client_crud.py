from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import client

def create_client(client: client.ClientCreate):
    db = SessionLocal()
    return client.create_client(db, client)

def get_client_by_token(token: str):
    db = SessionLocal()
    return client.get_client_by_token(db, token)
