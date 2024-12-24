from drf_spectacular.utils import (OpenApiParameter, extend_schema,
                                   extend_schema_view)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.external_currency.freecurrencyapi import convert
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
        result = convert(
            request.query_params['from'].upper(),
            request.query_params['to'].upper(),
            request.query_params['amount'],
        )
        return Response(
            {
                'query': request.query_params,
                'result': result
            }
        )
