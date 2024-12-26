"""Модуль для работы с freecurrencyapi сервисом."""

import os
from decimal import Decimal
from http import HTTPStatus
from typing import Union

import requests
from dotenv import load_dotenv

from api.external_currency.config import logger

load_dotenv()

APIKEY = os.getenv('APIKEY')

HEADERS = {'apikey': APIKEY}

ENDPOINTS = {
    'latest': 'https://api.freecurrencyapi.com/v1/latest',
    'status': 'https://api.freecurrencyapi.com/v1/status',
}
"""Методы сервиса, нужные для работы:

latest - возвращает последний курс валют по USD
status - возвращает статус по бесплатной лицензии

"""


def get_api_answer(endpoint: str) -> dict:
    """Обращается по методу сервиса и выдаёт данные.

    Args:
        endpoint (str): метод сервиса

    Returns:
        dict: json-словарь

    """
    try:
        response = requests.get(
            ENDPOINTS[endpoint],
            headers=HEADERS,
        )
        if response.status_code != HTTPStatus.OK:
            error_message = f'Ошибка: статус ответа = {response.status_code}'
            logger.error(error_message)
            raise Exception(error_message)
    except requests.RequestException as e:
        logger.error(f'Ошибка: попытка запроса = {e}')

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        error_message = f'Ошибка: формат ответа = {e}'
        logger.error(error_message)
        raise Exception(error_message)


def get_decimal(out: Union[int, float], to: Union[int, float],
                value: Union[int, float]) -> Decimal:
    """Производит расчет стоимости валюты.

    Args:
        out (int | float): значение валюты, из которой первести
        to (int | float): значение валюты, в которую первести
        value (int | float): количество для перевода

    Returns:
        decimal: результат расчёта
    """
    return Decimal(to) / Decimal(out) * Decimal(value)


def convert(out: str, to: str, value: Union[int, float]) -> Decimal:
    """Конвертирует по текущему курсу.

    Args:
        out (str): валюта, из которой первести
        to (str): валюта, в которую первести
        value (int | float): количество для перевода

    Returns:
        decimal: результат перевода
    """

    rates = get_api_answer('latest')['data']
    if out not in rates:
        error_message = f'Нет валюты {out}'
        logger.error(error_message)
        raise Exception(error_message)
    if to not in rates:
        error_message = f'Нет валюты {to}'
        logger.error(error_message)
        raise Exception(error_message)
    return get_decimal(rates.get(to), rates.get(out), value)
