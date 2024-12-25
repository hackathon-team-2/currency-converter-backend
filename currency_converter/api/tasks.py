from celery import shared_task
from django.core.cache import cache

from .constants import AVAILABLE_CURRENCY
from .external_currency.freecurrencyapi import get_api_answer


@shared_task
def load_currencies() -> None:
    """Получает значения валют и заносит их в кеш."""
    rates = get_api_answer('latest')['data']
    for rate in AVAILABLE_CURRENCY:
        cache.set(f'{rate}', rates.get(rate), timeout=3600*5)
