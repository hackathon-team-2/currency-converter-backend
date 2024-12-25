from django.core.cache import cache
from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.external_currency.freecurrencyapi import convert, get_decimal
from api.serializers import CurrencySerializer


@extend_schema_view(
    get=extend_schema(
        summary='Сконвертировать валюту',
        request=CurrencySerializer,
        responses={
            status.HTTP_200_OK: CurrencySerializer,
            status.HTTP_400_BAD_REQUEST: CurrencySerializer,
        },
        parameters=[
            OpenApiParameter(
                name='from',
                location=OpenApiParameter.QUERY,
                description='Валюта для конвертации',
                required=True,
                type=str),
            OpenApiParameter(
                name='to',
                location=OpenApiParameter.QUERY,
                description='Итоговая валюта ',
                required=True,
                type=str),
            OpenApiParameter(
                name='amount',
                location=OpenApiParameter.QUERY,
                description='Количество ',
                required=True,
                type=float),
        ],
    )
)
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
        # Проверяем, есть ли нужные значения в кеше:
        # Если нет, то отправляем запрос к апи
        if None in [from_cache, to_cache]:
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
