from typing import Iterable

from fastapi import APIRouter, FastAPI

__all__ = ("create",)


def create(
    *_,
    rest_routers: Iterable[APIRouter],
    **kwargs,
) -> FastAPI:
    """The application factory using FastAPI framework."""

    app = FastAPI(**kwargs)

    for router in rest_routers:
        app.include_router(router)

    return app
