from starlette.responses import JSONResponse

from src.entrypoints.schemas.schema import User as UserSchema, AnimalLocationDto
from src.services.animal_location_service import AnimalLocationService


async def create_animal_location(animal_location_dto: AnimalLocationDto):
    animal_location_service = AnimalLocationService()

    animal_location_response = animal_location_service.create_animal_location(animal_location_dto)
    return JSONResponse(content=animal_location_response, status_code=201)


async def get_all_animal_locations(has_not_expired: bool = True):
    animal_location_service = AnimalLocationService()

    params = transform_to_params(has_not_expired=has_not_expired)

    animal_location_response = animal_location_service.get_all_animal_locations(params)
    print("a")

    return JSONResponse(content=animal_location_response, status_code=200)


async def create_animal(user: UserSchema):
    return


def transform_to_params(**kwargs):
    return {k: v for k, v in kwargs.items() if v is not None}
