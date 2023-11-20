from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    token = Column(String, unique=True, index=True)

class ClientCreate(Client):
    pass

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client_by_token(db: Session, token: str):
    return db.query(Client).filter(Client.token == token).first()
