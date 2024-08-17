from abc import ABC, abstractmethod


class Parser(ABC):
    """ Абстрактный класс для работы с API """

    @staticmethod
    @abstractmethod
    def __connection_to_api(api_params):
        """ Приватный метод для подключения к API """
        pass

    @classmethod
    @abstractmethod
    def load_vacancies(cls, keyword):
        """ Метод для получения вакансий по ключевому слову """
        pass
