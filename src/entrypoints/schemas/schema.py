from typing import Optional

from pydantic import BaseModel


class AnimalLocationDto(BaseModel):
    description: Optional[str]
    latitude: str
    longitude: str
    s3_link: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": "Is a beautiful dog",
                "latitude": "-23.5505",
                "longitude": "-46.6333",
                "s3_link": "https://s3.amazonaws.com/animal-adoption-pictures/animal-location/1.jpg"
            }
        }


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

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "animal": {
                    "id": 1,
                    "name": "Dog",
                    "description": "Is a beautiful dog",
                    "specie": "Dog",
                    "birth_date": "2021-01-01"
                },
                "contact": {
                    "id": 1,
                    "name": "John Doe",
                    "phone": "11999999999",
                    "email": "john@gmail.com"
                }
            }
        }


class UserContact(BaseModel):
    name: str
    email: str
    phone: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@gmail.com",
                "phone": "11999999999"
            }
        }


class AnimalAdoptionDto(BaseModel):
    species: str
    name: str
    birth_date: str
    description: str
    contact: UserContact

    class Config:
        schema_extra = {
            "example": {
                "species": "dog",
                "name": "Dog",
                "birth_date": "2017-01-01",
                "description": "Is a beautiful dog",
                "contact": {
                    "name": "John Doe",
                    "email": "john@gmail.com",
                    "phone": "11999999999"

                }
            }
        }
