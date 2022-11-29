from src.entrypoints.schemas.schema import AnimalAdoptionDto
from src.models.models import Animal, UserAnimal, User
from src.repositories.base_repository import BaseRepository


class AnimalAdoptionRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserAnimal)

    def create_animal_adoption_model(self, animal_adoption_schema: AnimalAdoptionDto) -> UserAnimal:
        animal_created = Animal(
            name=animal_adoption_schema.name,
            description=animal_adoption_schema.description,
            specie=animal_adoption_schema.species,
            # birth_date=Daanimal_adoption_schema.birth_date,
        )
        animal = self.create(animal_created, commit=False)

        user_created = User(
            name=animal_adoption_schema.contact.name,
            email=animal_adoption_schema.contact.email,
            phone=animal_adoption_schema.contact.phone,
        )

        user = self.create(user_created, commit=False)

        user_animal_created = UserAnimal(
            animal=animal,
            user=user,
        )

        user_animal = self.create(user_animal_created, commit=True)

        return user_animal

    def get_user_animals_for_adoption(self, user_id: int) -> list:
        return self.db.session.query(UserAnimal).filter(UserAnimal.id_user == user_id).all()

    def get_all_animals_for_adoption(self) -> list:
        return self.db.session.query(UserAnimal).all()
