from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    """Properties to receive via API on creation.
    """    
    email: EmailStr
    password: str

    @validator('password', always=True)
    def validate_password1(cls, value):
        min_length = 8
        errors = ''
        if len(value) < min_length:
            errors += 'Password must be at least 8 characters long. '
        if not any(character.isupper() for character in value):
            errors += 'Password should contain at least one upercase character.'
        if errors:
            raise ValueError(errors)
            
        return value