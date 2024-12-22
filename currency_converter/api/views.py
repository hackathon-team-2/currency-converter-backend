import json

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import CurrencySerializer


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
        return Response({'data': request.query_params})
