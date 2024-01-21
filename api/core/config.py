import secrets

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Security Settings.
    """    
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 30 minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

settings = Settings()