from typing import Annotated

from fastapi import APIRouter, HTTPException, Response, Depends

from api.database import postgres_controler
from api.core import get_current_active_user
from api.schemas import User

signout_router = APIRouter()

@signout_router.post("/sign_out", description="Signout method to invalid user access.")
async def user_signout(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Delete user from database.

    :param current_user: email of active user
    :type current_user: Annotated[User, Depends
    :raises HTTPException: in case that token was invalid
    :return: http status 200 message.
    :rtype: FastAPI Response
    """    
    try:
        postgres_controler.deleter.delete_user(current_user)
    except:
        raise HTTPException(status_code=303, detail="User already checkout.")

    return Response(content="User deleted from database correctly.", status_code=200)