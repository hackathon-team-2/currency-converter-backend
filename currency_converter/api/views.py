from rest_framework.response import Response
from rest_framework.views import APIView

from api.external_currency.freecurrencyapi import convert
from api.serializers import CurrencySerializer


class CurrencyView(APIView):
    """
    Представление для обработки запроса:
    - используется базовый APIView
    - разрешён только get-метод
    - параметры для проверки передаются в сериализатор в контексте
    - после вызывается функция утилиты freecurrencyapi
    - результат выдаётся по формату: параметры запроса, результат
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
