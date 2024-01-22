from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from api.core import settings


class Security:
    """Security main class.
    """    
    __instance = None

    def __init__(self) -> None:
        """Security manager attributes.

        :raises Exception: Error in case of re-intancied try.
        """        
        if Security.__instance != None:
            raise Exception("Security class is a Singleton, cannot be created more than once.")
        else:
            Security.__instance = self
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def getInstance() -> Union[None, "Security"]:
        """Blocks second try of instance security class object.

        :return: None in case of Security object was already instancied or Security object in case was not.
        :rtype: Union[None, "Security"]
        """        
        if Security.__instance == None:
            Security()
        return Security.__instance


    def create_access_token(self,
        subject: Union[str, Any], expires_delta: timedelta = None
    ) -> str:
        """JWT creator.

        :param subject: _description_
        :type subject: Union[str, Any]
        :param expires_delta: _description_, defaults to None
        :type expires_delta: timedelta, optional
        :return: _description_
        :rtype: str
        """        
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode = {"exp": expire, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt


    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Check stored password and send password.

        :param plain_password: User send password
        :type plain_password: str
        :param hashed_password: Hashed stored password
        :type hashed_password: str
        :return: Coincidence confirmation.
        :rtype: bool
        """        
        return self.pwd_context.verify(plain_password, hashed_password)


    def get_password_hash(self, password: str) -> str:
        """Hashed password maker.

        :param password: Password to hash.
        :type password: str
        :return: Hashed password.
        :rtype: str
        """        
        return self.pwd_context.hash(password)
    
security_provider = Security()