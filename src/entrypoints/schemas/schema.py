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


class AnimalMinimalResponse(BaseModel):
    id: int
    name: str
    description: str
    specie: str
    birth_date: Optional[str]


class UserMinimalResponse(BaseModel):
    id: int
    name: str
    phone: Optional[str]
    email: Optional[str]


class AnimalAdoptionResponse(BaseModel):
    id: int
    animal: AnimalMinimalResponse
    contact: UserMinimalResponse
    created_at: str
    updated_at: str


class UserContact(BaseModel):
    name: str
    email: str
    phone: str


class AnimalAdoptionDto(BaseModel):
    species: str
    name: str
    birth_date: str
    description: str
    contact: UserContact
