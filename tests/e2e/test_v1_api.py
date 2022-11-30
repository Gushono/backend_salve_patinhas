import pytest
from starlette.testclient import TestClient

from app import app

test_client = TestClient(app)

generate_random_dict_animal_location = [
    {
        "description": "test",
        "latitude": "-23.5505",
        "longitude": "-46.6333",
        "s3_link": "https://s3.amazonaws.com/animal-adoption-pictures/animal-location/1.jpg",
    }
    for x in range(100)
]

generate_random_dict_animal_for_adoption = [
    {
        "species": "dog",
        "name": "Dog",
        "birth_date": "2017-01-01",
        "description": "Is a beautiful dog",
        "contact": {
            "name": "John Doe",
            "email": "john@gmail.com",
            "phone": f"1199999999{y}",
        },
    }
    for y in range(100)
]


class TestV1Api:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("animal_location", generate_random_dict_animal_location)
    def test_success_post_report_animal(
        self, run_alembic_upgrade_head, animal_location
    ):
        response = test_client.post("v1/report-animal", json=animal_location)
        print(generate_random_dict_animal_location)
        assert response.status_code == 201

    def test_success_get_all_animal_locations_has_not_expired_true(self):
        response = test_client.get("v1/animal-location?has_not_expired=True")
        assert response.status_code == 200

    def test_success_get_all_animal_locations_has_not_expired_false(self):
        response = test_client.get("v1/animal-location?has_not_expired=False")
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "animal_for_adoption", generate_random_dict_animal_for_adoption
    )
    def test_success_create_animal_for_adoption(
        self, run_alembic_upgrade_head, animal_for_adoption
    ):
        response = test_client.post("v1/animals-for-adoption", json=animal_for_adoption)
        assert response.status_code == 201

    def test_success_get_all_animals_for_adoption(self):
        response = test_client.get("v1/animals-for-adoption")
        assert response.status_code == 200

    def test_success_get_animal_for_adoption_by_user_id(self):
        response = test_client.get("v1/animals-for-adoption/user/1")
        assert response.status_code == 200

    def test_fail_post_report_animal(self):
        response = test_client.post("v1/report-animal", json={})
        assert response.status_code == 422
