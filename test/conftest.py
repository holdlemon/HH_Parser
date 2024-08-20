import pytest

from src.vacancy.vacancy import Vacancy


@pytest.fixture
def request_get():
    return {"items": [{"id": "93353083", "name": "Тестировщик комфорта квартир"}]}


@pytest.fixture
def load_vacancies_result():
    return [{"id": "93353083", "name": "Тестировщик комфорта квартир"}]


@pytest.fixture
def vacancy_data():
    return {
        "id": 1,
        "name": "Python Developer",
        "url": "http://example.com",
        "salary": {"from": 1000, "to": 2000},
        "requirement": "Experience with Python",
        "responsibility": "Develop web applications"
    }


@pytest.fixture
def vacancy(vacancy_data):
    return Vacancy(vacancy_data)
