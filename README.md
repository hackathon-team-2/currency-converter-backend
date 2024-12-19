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
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt  

```
# Структура 

## Конфиг для логирования
\external_currency\config.py

## openexchangerates сервис
Дока - https://docs.openexchangerates.org/reference/api-introduction
Для подключения нужен app_id, бесплатный тариф имеет ограничения  
Our popular Free Plan provides hourly updates (with base currency USD) and up to 1,000 requests/month.
Use https://docs.openexchangerates.org/reference/authentication to get App ID
