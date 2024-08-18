from abc import ABC, abstractmethod


class WorkingWithFile(ABC):
    """ Абстрактный класс для работы с файлами """

    @abstractmethod
    def save_to_file(self, vacancies: list[dict]) -> None:
        """Метод для сохранения в файл списка вакансий"""

        pass

    @abstractmethod
    def add_to_file(self, vacancies: list[dict]) -> None:
        """ Метод для добавления вакансий """

        pass

    @abstractmethod
    def get_from_file(self) -> list[dict]:
        """Метод для получения данных из файла"""

        pass

    @abstractmethod
    def delete_from_file(self) -> None:
        """Метод для удаления данных из файла"""

        pass
