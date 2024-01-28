import os

from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType

from api.core import mail_configuration, settings
from api.database import postgres_controler
from api.schemas import ForgetPasswordRequest

forget_password_router = APIRouter()

@forget_password_router.post("/forget-password")
async def forget_password(
    user: ForgetPasswordRequest,
    background_tasks: BackgroundTasks
):
    """Method to send email with active token as content to user

    :param user: user to send email.
    :type user: ForgetPasswordRequest
    :param background_tasks: background tasks that will be called after a response has been sent to the client.
    :type background_tasks: BackgroundTasks
    :raises HTTPException: In case of email connot be send it
    :return: message of mail confirmation
    :rtype: json
    """    
    try:
        if not isinstance(postgres_controler.reader.check_user_status(user.email), bool):
           raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                  detail="Invalid Email address")
            
        
        forget_url_link =  f"{os.environ.get('APP_HOST')}/recovery_password"
        
        email_body = { "company_name": os.environ.get("MAIL_FROM"),
                       "link_expiry_min": settings.ACCESS_TOKEN_EXPIRE_MINUTES,
                       "reset_link": forget_url_link }

        message = MessageSchema(
            subject="Password Reset Instructions",
            recipients=[user.email],
            template_body=email_body,
            subtype=MessageType.html
          )
       
        template_name = "mail/password_reset.html"

        fm = FastMail(mail_configuration)
        background_tasks.add_task(fm.send_message, message, template_name)

        return {"message": "Email has been sent", "success": True,
               "status_code": status.HTTP_200_OK}
    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                  detail="Email cannot be send it.")