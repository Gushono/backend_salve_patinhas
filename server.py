import os

from fastapi import FastAPI

from src.entrypoints.routers.router import add_routes
from fastapi_sqlalchemy import DBSessionMiddleware


def create_app(debug_mode: bool) -> FastAPI:
    app = FastAPI()
    add_routes(app)
    app.add_middleware(DBSessionMiddleware, db_url=os.getenv("DATABASE_URL"))

    if debug_mode:
        print(f"RUNNING ON DEBUG MODE, {debug_mode=}")
        app.debug = True

    return app

