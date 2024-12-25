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
    """Производит расчет стоимости валюты."""
    return Decimal(to) / Decimal(out) * Decimal(value)


def convert(out: str, to: str, value: Union[int, float]) -> Decimal:
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
    return get_decimal(rates.get(to), rates.get(out), value)
