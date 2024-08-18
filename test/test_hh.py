from unittest.mock import patch

import pytest
import requests

from src.working_with_api.hh import HH


def test_load_vacancies(request_get, load_vacancies_result):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = request_get
        assert HH.load_vacancies("test") == load_vacancies_result


def test_load_vacancies_error():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 201
        with pytest.raises(requests.RequestException):
            HH.load_vacancies("test")
