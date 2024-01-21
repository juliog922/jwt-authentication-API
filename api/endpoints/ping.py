from fastapi import APIRouter, HTTPException

from api.database import postgres_controler

ping_router = APIRouter()

@ping_router.get("/ping", description="Checks the availability and responsiveness of the API server.")
def ping():
    """Sends a simple request and expects a quick response, indicating that the server is up and running.

    :raises HTTPException: Error in case of database have not connection.
    :return: Pong response (the server is up and running).
    :rtype: json
    """    
    if postgres_controler.check_db_connection():
        return {"data": "pong"}
    else:
        raise HTTPException(status_code=503, detail="Database connection error")




