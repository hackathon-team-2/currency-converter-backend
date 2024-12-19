from openexchangerates import convert as oconvert
from freecurrencyapi import convert as fconvert

params = 'RUB', 'USD', 1000
print(oconvert(*params))
print(fconvert(*params))
