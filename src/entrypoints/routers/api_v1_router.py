from fastapi import APIRouter

from src.entrypoints.controllers.v1_api import create_animal, create_animal_location, get_all_animal_locations

api_v1 = APIRouter(prefix="/v1")

api_v1.add_api_route(
    path="/report-animal",
    endpoint=create_animal_location,
    methods=["POST"],
)

api_v1.add_api_route(
    path="/animal_location",
    endpoint=get_all_animal_locations,
    methods=["GET"],
)

api_v1.add_api_route(
    "/animal",
    create_animal,
    methods=["POST"],
    response_model_exclude_none=True,
)
