from src.working_with_api.hh import HH
from src.vacancy.vacancy import Vacancy
from src.working_with_file.working_to_json import WorkingToJSON


def user_interaction():
    print("Добро пожаловать в поиск вакансий на HeadHunter!")

    # Запрос поискового запроса у пользователя
    search_query = input("Введите поисковый запрос для запроса вакансий: ")

    # Загрузка вакансий
    vacancies_data = HH.load_vacancies(search_query)

    # Создание экземпляров класса Vacancy
    vacancies = [Vacancy(vacancy_data) for vacancy_data in vacancies_data]

    # Создание экземпляра класса WorkingToJSON для работы с файлом
    json_saver = WorkingToJSON()

    while True:
        print("\nВыберите действие:")
        print("1. Получить топ N вакансий по зарплате")
        print("2. Получить вакансии с ключевым словом в описании")
        print("3. Сохранить вакансии в файл")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            # Запрос количества вакансий для отображения в топе по зарплате
            top_n = int(input("Введите количество вакансий для отображения в топе по зарплате: "))
            top_vacancies = Vacancy.get_top_salary_vacancies(vacancies, top_n)
            for vacancy in top_vacancies:
                print(vacancy)

        elif choice == "2":
            # Запрос ключевого слова для фильтрации вакансий по описанию
            keyword = input("Введите ключевое слово для фильтрации вакансий по описанию: ")
            filtered_vacancies = Vacancy.filter_by_keywords(vacancies, [keyword])
            for vacancy in filtered_vacancies:
                print(vacancy)

        elif choice == "3":
            # Сохранение вакансий в файл
            vacancies_dicts = [vacancy.get_attributes() for vacancy in vacancies]
            json_saver.add_to_file(vacancies_dicts)
            print("Вакансии успешно сохранены в файл.")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    user_interaction()
