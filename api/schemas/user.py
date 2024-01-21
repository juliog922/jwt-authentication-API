from typing import Optional

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """User Shared properties.
    """    
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_admin: bool = False

class UserCreate(UserBase):
    """Properties to receive via API on creation.
    """    
    email: EmailStr
    password: str

class UserUpdate(UserBase):
    """Properties to receive via API on update.
    """    
    password: Optional[str] = None

class UserInDBBase(UserBase):
    """Additional properties to return via API.
    """    
    id: Optional[int] = None

class UserInDB(UserInDBBase):
    """Additional properties stored in DB.
    """    
    hashed_password: str