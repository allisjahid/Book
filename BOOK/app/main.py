from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2BearerToken
from app.crud import book_crud, author_crud, client_crud
from app.security import get_current_client

app = FastAPI()

oauth2_scheme = OAuth2BearerToken(tokenUrl="token")

@app.post("/token")
async def login(client: client_crud.Client):
    return {"access_token": client["full_name"], "token_type": "bearer"}

@app.get("/books/", response_model=list[book_crud.Book])
async def get_books(title_startswith: str = None, author_id: int = None):
    return book_crud.get_books(title_startswith=title_startswith, author_id=author_id)

@app.post("/books/", response_model=book_crud.Book)
async def create_book(book: book_crud.BookCreate):
    return book_crud.create_book(book)

# Add other API methods as needed (edit book, add author, create client, link/unlink client and book)

@app.get("/client/books/", response_model=list[book_crud.Book])
async def get_client_books(token: str = Depends(oauth2_scheme)):
    client = get_current_client(token)
    if not client:
        raise HTTPException(status_code=401, detail="Invalid token")
    return book_crud.get_client_books(client["id"])
