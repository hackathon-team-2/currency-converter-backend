"""Модуль для работы с freecurrencyapi сервисом."""

from decimal import Decimal
from dotenv import load_dotenv
import os
from http import HTTPStatus
import requests

from config import logger

load_dotenv()

APIKEY = os.getenv('APIKEY')

HEADERS = {'apikey': APIKEY}

"""Некоторые методы сервиса, нужные для работы."""
ENDPOINTS = {
    'latest': 'https://api.freecurrencyapi.com/v1/latest',
    'status': 'https://api.freecurrencyapi.com/v1/status',
}


def get_api_answer(endpoint: str) -> dict:
    """
    Обращается по методу сервиса и выдаёт данные.
    """
    try:
        response = requests.get(
            ENDPOINTS[endpoint],
            headers=HEADERS,
        )
        if response.status_code != HTTPStatus.OK:
            logger.error('Это не 200')
            raise Exception('Неуспешно')
    except requests.RequestException:
        logger.error('Ошибка запроса')

    try:
        return response.json()
    except ValueError:
        logger.error('Where is json format?')
        raise Exception('Where is json format?')


def convert(out: str, to: str, value) -> Decimal:
    """Конвертирует по текущему курсу."""
    rates = get_api_answer('latest')['data']
    if out not in rates:
        error_message = f'Нет валюты {out}'
        logger.error(error_message)
        raise Exception(error_message)
    if to not in rates:
        error_message = f'Нет валюты {to}'
        logger.error(error_message)
        raise Exception(error_message)
    return Decimal(rates.get(to)) / Decimal(rates.get(out)) * Decimal(value)


if __name__ == '__main__':
    # For example
    result = convert('RUB', 'EUR', 10000)
    print(result)
