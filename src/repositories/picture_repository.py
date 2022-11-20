from pydantic import BaseModel

from src.entrypoints.schemas.schema import PictureDto
from src.models.models import PictureModel
from src.repositories.base_repository import BaseRepository


class PictureRepository(BaseRepository):
    def __init__(self):
        super().__init__(PictureModel)

    def create_picture(self, picture_schema: PictureDto) -> PictureModel:
        picture_model = PictureModel(**picture_schema.dict())
        return self.create(picture_model, commit=False)
