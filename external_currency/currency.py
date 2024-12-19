"""Модуль для работы с openexchangerates сервисом."""

from decimal import Decimal
from dotenv import load_dotenv
import os
from http import HTTPStatus
import requests

from config import logger

load_dotenv()
APPID = os.getenv('APPID')
HEADERS = {'accept': 'application/json'}

"""Некоторые методы сервиса, нужные для работы."""
ENDPOINTS = {
    'usage': f'https://openexchangerates.org/api/usage.json?app_id={APPID}',
    'latest': f'https://openexchangerates.org/api/latest.json?app_id={APPID}',
    'currencies': f'https://openexchangerates.org/api/currencies.json?app_id={APPID}',
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


def check_currency(currency: str) -> bool:
    """Проверяет, есть ли заданная валюта в списке возможных."""
    return currency in get_api_answer('currencies')


def convert(out: str, to: str, value) -> Decimal:
    """Конвертирует по текущему курсу."""
    rates = get_api_answer('latest')['rates']
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
    params = 'RUB', 'USD', 1000
    print(convert(*params))
