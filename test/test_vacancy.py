from src.vacancy.vacancy import Vacancy


def test_vacancy_str(vacancy):
    expected_str = "ID вакансии:1, название:Python Developer, ссылка:http://example.com, зарплата:2000, описание:Experience with Python"
    assert str(vacancy) == expected_str


def test_vacancy_lt(vacancy):
    other_vacancy = Vacancy({"id": 2, "name": "Java Developer", "url": "http://example.com", "salary": 1500, "requirement": "Experience with Java"})
    assert vacancy > other_vacancy


def test_vacancy_filter_by_keywords():
    vacancies = [
        Vacancy({"id": 1, "name": "Python Developer", "url": "http://example.com", "salary": 2000, "requirement": "Experience with Python"}),
        Vacancy({"id": 2, "name": "Java Developer", "url": "http://example.com", "salary": 1500, "requirement": "Experience with Java"})
    ]
    filtered_vacancies = Vacancy.filter_by_keywords(vacancies, ["Python"])
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0].id == 1


def test_vacancy_get_top_salary_vacancies():
    vacancies = [
        Vacancy({"id": 1, "name": "Python Developer", "url": "http://example.com", "salary": 2000, "requirement": "Experience with Python"}),
        Vacancy({"id": 2, "name": "Java Developer", "url": "http://example.com", "salary": 1500, "requirement": "Experience with Java"}),
        Vacancy({"id": 3, "name": "JavaScript Developer", "url": "http://example.com", "salary": 2500, "requirement": "Experience with JavaScript"})
    ]
    top_vacancies = Vacancy.get_top_salary_vacancies(vacancies, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].id == 3
    assert top_vacancies[1].id == 1
