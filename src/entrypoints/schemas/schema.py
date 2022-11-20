from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str = None
    age: int

    class Config:
        orm_mode = True


class AnimalLocationDto(BaseModel):
    description: Optional[str]
    latitude: str
    longitude: str
    s3_link: str

    class Config:
        orm_mode = True


class PictureDto(BaseModel):
    s3_link: str
