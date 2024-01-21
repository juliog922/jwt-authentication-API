from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """JWT Token attributes.
    """    
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """Token user id and exiperd time.
    """    
    sub: Optional[int] = None
    exp: Optional[int] = None