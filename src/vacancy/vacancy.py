from typing import Any


class Vacancy:
    """ Класс для работы с вакансиями """
    id: int
    name: str
    url: str
    salary: int
    requirement: str
    responsibility: str
    __slots__ = ("id", "name", "url", "salary", "requirement", "responsibility")

    def __init__(self, data: dict) -> None:
        """ Конструктор класса """
        for attr in self.__slots__:
            if attr in data:
                setattr(self, attr, data[attr])
        self.salary = self.__validate_salary(self.salary)
        if not hasattr(self, "requirement") or self.requirement is None:
            self.requirement = "Описание отсутствует"

    def __str__(self) -> str:
        """ Получение информации о вакансии """

        return f"ID вакансии:{self.id}, название:{self.name}, ссылка:{self.url}, зарплата:{self.salary}, описание:{self.requirement}"

    @staticmethod
    def __validate_salary(salary: Any) -> int:
        """ Метод для валидации зарплаты """
        if isinstance(salary, dict):
            if 'to' in salary and salary['to'] is not None:
                return salary['to']
            elif 'from' in salary and salary['from'] is not None:
                return salary['from']
            else:
                return 0
        elif salary is None:
            return 0
        else:
            return salary

    def __lt__(self, other: Any) -> Any:
        """ Метод сравнения зарплаты для оператора - < """
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        raise TypeError

    def __eq__(self, other: Any) -> Any:
        """ Метод сравнения зарпалаты для оператора равенства - == """
        if isinstance(other, Vacancy):
            return self.__validate_salary == other.__validate_salary
        raise TypeError

    def get_attributes(self) -> dict:
        """ Метод для получения атрибутов, указанных в __slots__ """
        return {attr: getattr(self, attr) for attr in self.__slots__ if hasattr(self, attr)}

    @staticmethod
    def filter_by_keywords(vacancies: list, keywords: list) -> list:
        """Оставляет в списке только те вакансии, которые содержат ключевые слова в названии,
        требованиях или обязанностях
        """

        filtered_vacancies = []
        for vacancy in vacancies:
            string_for_searching = (vacancy.name + str(vacancy.requirement)).lower()
            check_status = True
            for keyword in keywords:
                if keyword.lower() not in string_for_searching:
                    check_status = False
                    break
            if check_status:
                filtered_vacancies.append(vacancy)

        return filtered_vacancies

    @staticmethod
    def get_top_salary_vacancies(vacancies: list, top_n: int) -> list:
        """Метод для получения ТОП-n вакансий по зарплате"""

        valid_vacancies = [vacancy for vacancy in vacancies if isinstance(vacancy, Vacancy)]
        sorted_vacancies = sorted(valid_vacancies, key=lambda x: x.salary, reverse=True)
        return sorted_vacancies[:top_n]


# if __name__ == "__main__":
#     res1 = Vacancy(2146816, "DENUM GROUP",  "https://api.hh.ru/employers/2146816", 70000, "Работать")
#     res2 = Vacancy(222111, "Python разработчик", "hh.ru", 70000, "Работать")
#     print(res1.salary == res2.salary)
