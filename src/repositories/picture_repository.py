import os

import boto3 as boto3

from src.entrypoints.schemas.schema import PictureDto
from src.models.models import PictureModel
from src.repositories.base_repository import BaseRepository


class PictureRepository(BaseRepository):
    def __init__(self):
        super().__init__(PictureModel)

    def create_picture(self, picture_schema: PictureDto) -> PictureModel:
        picture_model = PictureModel(**picture_schema.dict())
        return self.create(picture_model, commit=False)

    # @staticmethod
    # def upload_picture_to_s3(picture: PictureDto):
    #     s3 = boto3.client(
    #         "s3",
    #         aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    #         aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    #     )
    #
    #     # response = s3.upload_fileobj(
    #     #     picture.file,
    #     #     os.getenv("AWS_S3_BUCKET"),
    #     #     picture.filename,
    #     # )


