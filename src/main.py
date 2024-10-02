from fastapi import APIRouter, FastAPI

from src.config import settings
from src.infrastructure.application import create as application_factory

rest_routers: list[APIRouter] = []

app: FastAPI = application_factory(
    title=settings.public_api.name,
    version=settings.public_api.version,
    debug=settings.debug,
    rest_routers=rest_routers,
)
