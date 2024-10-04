from fastapi import APIRouter, FastAPI

from src import rest
from src.config import settings
from src.infrastructure.application import create as application_factory

rest_routers: tuple[APIRouter, ...] = (
    rest.code_assistance.rest.router,
    rest.finances.rest.router,
    rest.research.rest.router,
)

app: FastAPI = application_factory(
    title=settings.public_api.name,
    version=settings.public_api.version,
    debug=settings.debug,
    rest_routers=rest_routers,
)
