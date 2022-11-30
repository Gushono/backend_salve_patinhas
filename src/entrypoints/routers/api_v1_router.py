from fastapi import APIRouter

from src.entrypoints.controllers.v1_api import create_animal_location, get_all_animal_locations, \
    create_animal_for_adoption, get_user_animals_for_adoption, get_all_animals_for_adoption
from src.entrypoints.schemas.schema import AnimalAdoptionResponse
from src.services.animal_location_service import AnimalLocationResponse

api_v1 = APIRouter(prefix="/v1")

api_v1.add_api_route(
    path="/report-animal",
    endpoint=create_animal_location,
    methods=["POST"],
    response_model=AnimalLocationResponse,
)

api_v1.add_api_route(
    path="/animal-location",
    endpoint=get_all_animal_locations,
    methods=["GET"],
    response_model=list[AnimalLocationResponse],
)

api_v1.add_api_route(
    "/animals-for-adoption",
    create_animal_for_adoption,
    methods=["POST"],
    response_model=AnimalAdoptionResponse,
    response_model_exclude_none=True,

)

api_v1.add_api_route(
    "/animals-for-adoption",
    get_all_animals_for_adoption,
    methods=["GET"],
    response_model=list[AnimalAdoptionResponse],
    response_model_exclude_none=True,
)

api_v1.add_api_route(
    "/animals-for-adoption/user/{user_id}",
    get_user_animals_for_adoption,
    methods=["GET"],
    response_model=list[AnimalAdoptionResponse],
    response_model_exclude_none=True,
)
