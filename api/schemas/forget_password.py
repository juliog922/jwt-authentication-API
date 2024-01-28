from pydantic import BaseModel, validator, EmailStr

class ForgetPasswordRequest(BaseModel):
    """Necesary attribute for password recovery
    """    
    email: EmailStr

class ResetForgetPassword(BaseModel):
    """Recovery password structure
    """    
    new_password: str
    confirm_password: str

    @validator("confirm_password")
    def passwords_match(cls, confirm_password, values):
        """Check if passwords match

        :param confirm_password: Password clone
        :type confirm_password: str
        :param values: dictionary of attributes
        :type values: dict
        :raises ValueError: In case that not match
        :return: Password post-validation
        :rtype: str
        """        
        if "new_password" in values and confirm_password != values["new_password"]:
            raise ValueError("Passwords do not match")
        return confirm_password