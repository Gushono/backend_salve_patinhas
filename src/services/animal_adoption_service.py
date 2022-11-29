from src.entrypoints.schemas.schema import AnimalAdoptionResponse, UserMinimalResponse, AnimalAdoptionDto, \
    AnimalMinimalResponse
from src.models.models import UserAnimal
from src.repositories.animal_adoption_repository import AnimalAdoptionRepository


class AnimalAdoptionService:
    def __init__(self, animal_adoption_repository=None):
        self.animal_adoption_repository = animal_adoption_repository or AnimalAdoptionRepository()

    def create_animal_adoption(self, animal_adoption_schema: AnimalAdoptionDto) -> dict:
        user_animal_model = self.animal_adoption_repository.create_animal_adoption_model(animal_adoption_schema)

        return self.parse_object_to_response(user_animal_model)

    async def get_user_animals_for_adoption(self, user_id: int) -> list:
        user_animals = self.animal_adoption_repository.get_user_animals_for_adoption(user_id)

        return [
            self.parse_object_to_response(user_animal_model) for user_animal_model in user_animals
        ]

    async def get_all_animals_for_adoption(self) -> list:
        user_animals = self.animal_adoption_repository.get_all_animals_for_adoption()

        return [
            self.parse_object_to_response(user_animal_model) for user_animal_model in user_animals
        ]

    @staticmethod
    def parse_object_to_response(user_animal: UserAnimal):
        return AnimalAdoptionResponse.parse_obj(
            {
                "id": user_animal.id,
                "animal": AnimalMinimalResponse.parse_obj(user_animal.animal.__dict__).dict(),
                "contact": UserMinimalResponse(
                    id=user_animal.user.id,
                    name=user_animal.user.name,
                    phone=user_animal.user.phone
                ).dict(),
                "created_at": str(user_animal.created_at),
                "updated_at": str(user_animal.updated_at),
            }
        ).dict()
