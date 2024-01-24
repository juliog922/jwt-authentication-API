from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from api.core import settings
from api.database import postgres_controler

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_active_user(token: Annotated[str, Depends(oauth2_scheme)]) -> str:
    """Main dependencie function

    :param token: Json Web Token
    :type token: Annotated[str, Depends]
    :raises credentials_exception: Could not validate credentials
    :return: email of user in case of active status.
    :rtype: str
    """    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    if not postgres_controler.reader.check_user_status(email):
        raise credentials_exception
    return email
