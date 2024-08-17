import requests

from src.working_with_api.abstract_parser import Parser


class HH(Parser):
    """ Класс для работы с API HeadHunter """
    @staticmethod
    def __connection_to_api(api_params):
        """Приватный метод для подключения к API"""
        url = "https://api.hh.ru/vacancies"
        headers = {"User-Agent": "HH-User-Agent"}

        response = requests.get(url, headers=headers, params=api_params)

        if response.status_code != 200:
            raise requests.RequestException
        return response

    @classmethod
    def load_vacancies(cls, keyword):
        """Метод для получения вакансий по ключевому слову"""

        params = {"text": keyword, "page": 0, "per_page": 100, "area": 113}
        vacancies = []

        while params.get("page") != 1:
            vacancies_page = cls.__connection_to_api(params).json()["items"]
            vacancies.extend(vacancies_page)
            params["page"] += 1

        return vacancies


if __name__ == "__main__":
    res = HH.load_vacancies("python")
    print(res)
