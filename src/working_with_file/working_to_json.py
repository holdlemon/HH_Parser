import json
import os

from src.working_with_file.abstract_working_with_file import WorkingWithFile


class WorkingToJSON(WorkingWithFile):
    """ Класс для работы с JSON-файлами """

    __file_name: str
    path_to_file: str

    def __init__(self, file_name: str = "vacancies.json", path_to_file: str = "../../data/") -> None:
        """ Конструктор класса """

        self.__file_name = file_name
        self.path_to_file = path_to_file
        os.makedirs(self.path_to_file, exist_ok=True)

    def save_to_file(self, vacancies: list[dict]) -> None:
        """ Метод для сохранения вакансий в файл """

        with open(self.path_to_file + self.__file_name, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def add_to_file(self, vacancies: list[dict]) -> None:
        """ Метод добавления вакансии """
        existing_vacancies = self.get_from_file()
        existing_ids = {vacancy['id'] for vacancy in existing_vacancies}

        new_vacancies = [vacancy for vacancy in vacancies if vacancy['id'] not in existing_ids]

        all_vacancies = existing_vacancies + new_vacancies
        self.save_to_file(all_vacancies)

    def get_from_file(self) -> list[dict]:
        """Метод для получения данных из файла"""

        with open(self.path_to_file + self.__file_name, "r", encoding="utf-8") as file:
            return json.load(file)

    def delete_from_file(self) -> None:
        """Метод для удаления данных из файла"""

        self.save_to_file([])


# if __name__ == "__main__":
#     wf = WorkingToJSON()
#     wf.save_to_file([{"id":"105832313","premium":False,"name":"Курьер - Сборщик","department":None,"has_test":False,"response_letter_required":False,"area":{"id":"43","name":"Калуга","url":"https://api.hh.ru/areas/43"},"salary":{"from":69600,"to":128750,"currency":"RUR","gross":False},"type":{"id":"open","name":"Открытая"},"address":False,"response_url":False,"sort_point_distance":False,"published_at":"2024-08-15T09:04:14+0300","created_at":"2024-08-15T09:04:14+0300","archived":False,"apply_alternate_url":"https://hh.ru/applicant/vacancy_response?vacancyId=105832313","show_logo_in_search":False,"insider_interview":False,"url":"https://api.hh.ru/vacancies/105832313?host=hh.ru","alternate_url":"https://hh.ru/vacancy/105832313"}])
#     # print(wf.delete_from_file())
