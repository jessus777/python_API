from fastapi import FastAPI
from src.infraestructure.web.api.request_api import grimoire_route

app = FastAPI()

app.include_router(grimoire_route, prefix="/api/v1")
