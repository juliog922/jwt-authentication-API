from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from api.database import postgres_controler
from api.core import security_provider, settings
from api.schemas import Token

login_router = APIRouter()

@login_router.post("/login", description="Login method that provide access token.")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """Endpoint to grant access to user throug access token.

    :param form_data: data provide from user
    :type form_data: Annotated[OAuth2PasswordRequestForm, Depends
    :raises HTTPException: In case that user type incorrect password or is not created on database.
    :return: Access token response.
    :rtype: Token
    """    
    hashed_password = postgres_controler.reader.get_hashed_password(form_data.username)

    if not hashed_password or not security_provider.verify_password(form_data.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = security_provider.create_access_token(
        subject={"sub": form_data.username}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")