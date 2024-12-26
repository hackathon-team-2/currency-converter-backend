from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

from api import openapi
from api.external_currency.freecurrencyapi import convert, get_decimal
from api.serializers import CurrencySerializer


@openapi.currency
class CurrencyView(APIView):
    """
    Чтобы сконвертировать одну валюту в другую,
    используйте запрос с параметрами: from, to, amount.
    """

    def get(self, request, *args, **kwargs):
        serializer = CurrencySerializer(
            data=request.data,
            context={
                'request': request,
                'params': request.query_params,
                }
        )
        serializer.is_valid(raise_exception=True)

        from_param = request.query_params['from'].upper()
        to_param = request.query_params['to'].upper()
        amount_param = request.query_params['amount']

        from_cache = cache.get(from_param)
        to_cache = cache.get(to_param)
        # Проверяем, есть ли нужные значения в кэше:
        # Если нет, то отправляем запрос к апи
        if from_cache and to_cache:
            result = convert(
                from_param, to_param, amount_param
            )
            return Response(
                {
                    'query': request.query_params,
                    'result': result
                }
            )
        # Если есть, то берем значения из кэша:
        result = get_decimal(
            from_cache, to_cache, amount_param
        )
        return Response(
            {
                'query': request.query_params,
                'result': result
            }
        )
