# currency-converter-backend
currency exchange service


# .env
Use .env.example to make your own .env  


# Установка
```bash
git clone https://github.com/hackathon-team-2/currency-converter-backend.git
```

```bash
python -m venv venv
. venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt  
cd currency_converter  
python manage.py migrate  
python manage.py runserver  
```
Go to http://127.0.0.1:8000/convert/?from=USD&to=EUR&amount=100  

# Структура 

## Приложение api - сервис для конвертации валюты
Структура запроса:  
{
    "from": "USD",
    "to": "RUB",
    "amount": 25000
}  
Структура ответа:  
{
  "query": {
    "from": "USD",
    "to": "RUB",
    "amount": 25000
   },
  "result": 2590593.3413124997
}
### Реализация
- Вью для get-запроса и обработки параметров  
- Сериализатор для проверки параметров: наличие, соответствие    

## freecurrencyapi сервис - сторонний сервис
 api/external_currency/  
Дока - https://freecurrencyapi.com/docs/  
Для подключения нужен apikey, бесплатный тариф имеет ограничения  
5k Free Monthly Requests + 32 World Currencies + All exchange rates are updated on a daily basis.  

### Конфиг для логирования
/api/external_currency/config.py


## Примеры для теста
http://127.0.0.1:8000/convert?from=USD&to=EUR&amount=100  
http://127.0.0.1:8000/convert?from=rub&to=USD&amount=100  
http://127.0.0.1:8000/convert?from=RUB&to=eur&amount=100  
http://127.0.0.1:8000/convert?from=rub&to=qqq&amount=100  
http://127.0.0.1:8000/convert?from=RUB&to=qqq&amount=100  

