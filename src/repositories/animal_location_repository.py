from datetime import datetime

from fastapi_sqlalchemy import db

from src.entrypoints.schemas.schema import AnimalLocationDto
from src.models.models import AnimalLocationModel, PictureModel
from src.repositories.base_repository import BaseRepository


class AnimalLocationRepository(BaseRepository):
    def __init__(self):
        super().__init__(AnimalLocationModel)

    def create_animal_location(
        self,
        animal_location_schema: AnimalLocationDto,
        picture_model: PictureModel = None
    ) -> AnimalLocationModel:
        animal_location_model = AnimalLocationModel(**animal_location_schema.dict(exclude_none=True))
        animal_location_model.picture = picture_model

        return self.create(animal_location_model)

    def get_all_animal_locations(self, params):
        if params.get("has_not_expired"):
            return db.session.query(AnimalLocationModel).filter(
                AnimalLocationModel.expires_at > datetime.now()
            ).all()

        return self.get_all()
