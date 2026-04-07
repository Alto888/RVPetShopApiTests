import allure
import jsonschema
import requests
from .schemas.pet_schema import PET_SCHEMA

BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature("Pet")
class TestPet:
    @allure.title("Добавление нового питомца")
    def test_add_pet(self):
        with allure.step ("Подготовка данных для создания питомца"):
            payload = {
                "id": 10,
                "name": "doggie",
                "category": {
                    "id": 1,
                    "name": "Dogs"
                },
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            }
        with allure.step ("Отправка запроса на создание питомца"):
            response = requests.post (url=f"{BASE_URL}/pet", json=payload)
            response_json = response.json()
        with allure.step ("Проверка статуса ответа и валидация Json схемы"):
            assert response.status_code == 404
            jsonschema.validate(response_json, PET_SCHEMA)
        with allure.step ("Проверка параметров питомца в ответе"):
            assert response_json ['id'] == payload['id'], "id питомца не совпадает с ожидаемым"
            assert response_json ['name'] == payload['name'], "name питомца не совпадает с ожидаемым"
            assert response_json ['status'] == payload['status'], "status питомца не совпадает с ожидаемым"



