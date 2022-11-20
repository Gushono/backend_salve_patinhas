from fastapi import FastAPI

from src.entrypoints.routers.api_v1_router import api_v1


def add_routes(app: FastAPI) -> None:
    app.include_router(api_v1)
