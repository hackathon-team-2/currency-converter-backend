from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import CurrencySerializer

from external_currency.freecurrencyapi import convert


class CurrencyView(APIView):

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
            request.query_params['from'],
            request.query_params['to'],
            request.query_params['amount'],
        )
        return Response(
            {
                'query': request.query_params,
                'result': result
            }
        )
