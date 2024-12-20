# currency-converter-backend
currency exchange service


# .env
Use .env.example to make your own .env  


# Setup
```bash
git clone #АКТУАЛЬНАЯ ССЫЛКА
```

```bash
python -m venv venv
. venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt  

```
# Структура 

## Конфиг для логирования
\external_currency\config.py

## freecurrencyapi сервис
Дока - https://freecurrencyapi.com/docs/
Для подключения нужен apikey, бесплатный тариф имеет ограничения  
5k Free Monthly Requests + 32 World Currencies + All exchange rates are updated on a daily basis.

### How to use?
Go to external_currency\example.py -> Run
