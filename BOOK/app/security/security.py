from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2BearerToken
from app.crud import client_crud

oauth2_scheme = OAuth2BearerToken(tokenUrl="token")

def get_current_client(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    client = client_crud.get_client_by_token(token)
    if client is None:
        raise credentials_exception
    return client
