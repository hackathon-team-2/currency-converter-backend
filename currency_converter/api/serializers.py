from rest_framework import serializers

from api.constants import AVAILABLE_CURRENCY


class CurrencySerializer(serializers.Serializer):
    """
    Проверяет наличие всех параметров
    Проверяет валюты из списка доступных (список в constants)
    Проверяет тип для количества
    """

    def validate(self, data):
        out = self.context['params'].get('from')
        to = self.context['params'].get('to')
        amount = self.context['params'].get('amount')
        if not out:
            raise serializers.ValidationError('Введите валюту "из"')
        if out not in AVAILABLE_CURRENCY:
            raise serializers.ValidationError(
                f'Введите доступную валюту из списка: {AVAILABLE_CURRENCY}')
        if not to:
            raise serializers.ValidationError('Введите валюту "в"')
        if out not in AVAILABLE_CURRENCY:
            raise serializers.ValidationError(
                f'Введите доступную валюту из списка: {AVAILABLE_CURRENCY}')
        if not amount:
            raise serializers.ValidationError('Введите количество')
        if not (amount.replace('.', '', 1)).isdigit():
            raise serializers.ValidationError('Проверьте тип количества')
        return data
