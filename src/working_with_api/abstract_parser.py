from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    """ Абстрактный класс для работы с API """

    @staticmethod
    @abstractmethod
    def __connection_to_api(api_params: dict) -> Any:
        """ Приватный метод для подключения к API """
        pass

    @classmethod
    @abstractmethod
    def load_vacancies(cls, keyword: str) -> list:
        """ Метод для получения вакансий по ключевому слову """
        pass
