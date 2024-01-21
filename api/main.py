from fastapi import FastAPI

from api.endpoints import ping_router

app = FastAPI()
app.include_router(ping_router)