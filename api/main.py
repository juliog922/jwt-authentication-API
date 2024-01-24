from fastapi import FastAPI

from api.endpoints import (
    ping_router,
    sign_in_router)

app = FastAPI()
app.include_router(ping_router)
app.include_router(sign_in_router)