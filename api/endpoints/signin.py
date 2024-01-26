from fastapi import APIRouter, HTTPException, Response

from api.database import postgres_controler
from api.core import security_provider
from api.schemas import User

sign_in_router = APIRouter()

@sign_in_router.post("/sign_in", description="Create new user into database.")
def save_new_user(user: User):
    """Add new user to database

    :param user: User schema with all user attributes.
    :type user: UserCreate
    :raises HTTPException: In case of user already exists
    :return: Successfull sign in message.
    :rtype: Response
    """    
    hashed_password = security_provider.get_password_hash(user.password)
    try:
        postgres_controler.creator.create_user(
            user.email,
            hashed_password,
            False,
            False
            )
    except:
        raise HTTPException(status_code=303, detail="User already exists.")
    return Response(content="User created correctly.", status_code=200)