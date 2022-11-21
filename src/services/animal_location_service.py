from typing import Optional

from pydantic import BaseModel

from src.entrypoints.schemas.schema import AnimalLocationDto, PictureDto
from src.repositories.animal_location_repository import AnimalLocationRepository
from src.repositories.picture_repository import PictureRepository


class AnimalLocationResponse(BaseModel):
    id: int
    latitude: str
    longitude: str
    s3_link: Optional[str]
    expires_at: str
    created_at: str
    updated_at: str


class AnimalLocationService:
    def __init__(
        self,
        animal_location_repository: AnimalLocationRepository = None,
        picture_repository: PictureRepository = None
    ):
        self.animal_location_repository = animal_location_repository or AnimalLocationRepository()
        self.picture_repository = picture_repository or PictureRepository()

    def create_animal_location(self, animal_location_schema: AnimalLocationDto) -> dict:
        print("Esse é o debug.")
        s3_link = animal_location_schema.s3_link
        animal_location_schema.s3_link = None

        picture_model = self.picture_repository.create_picture(
            PictureDto(s3_link=s3_link)
        )

        animal_location_model = self.animal_location_repository.create_animal_location(
            animal_location_schema,
            picture_model
        )

        return AnimalLocationResponse.parse_obj(
            {
                "id": animal_location_model.id,
                "latitude": animal_location_model.latitude,
                "longitude": animal_location_model.longitude,
                "s3_link": animal_location_model.picture.s3_link,
                "expires_at": str(animal_location_model.expires_at),
                "created_at": str(animal_location_model.created_at),
                "updated_at": str(animal_location_model.updated_at),
            }
        ).dict()

    def get_all_animal_locations(self, params=None):
        models = self.animal_location_repository.get_all_animal_locations(params)
        print(models[0])
        return [AnimalLocationResponse.parse_obj(
            {
                "id": model.id,
                "latitude": model.latitude,
                "longitude": model.longitude,
                "expires_at": str(model.expires_at),
                "created_at": str(model.created_at),
                "updated_at": str(model.updated_at),
            }
        ).dict() for model in models]
