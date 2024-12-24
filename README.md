# Проект: 
Сервис для конвертации валют.  

## Содержание
- [Технологии](#технологии)
- [Запуск проекта](#запуск-проекта)
- [Структура проекта](#структура-проекта)
- [Развёртывание](#развёртывание)



## Технологии:
### Frontend
ДОПИСАТЬ

### Backend
Python + Django REST Framework + drf-spectacular + Redis + Celery + Nginx + Docker + GitHub Actions 



## Запуск проекта
1. Склонируйте проекта с git-репозитория 
```bash
git clone https://github.com/hackathon-team-2/currency-converter-backend.git
```
2. Используйте .env.example и сделайте свой .env. 
APIKEY-токен можно получить здесь - https://freecurrencyapi.com/

3. В терминал последовательно выполните команды:

```bash
python -m venv venv
. venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt  
cd currency_converter  
python manage.py migrate  
python manage.py runserver  
```

4. Проект станет доступен по ссылке http://127.0.0.1:8000/convert/?from=USD&to=EUR&amount=1000  
![drf_interface](https://github.com/hackathon-team-2/currency-converter-backend/blob/main/drf_interface.png)


5. Подробное описание станет доступно по ссылке http://127.0.0.1:8000/api/schema/swagger-ui/  
![swagger_interface](https://github.com/hackathon-team-2/currency-converter-backend/blob/main/swagger_interface.png)

## Структура проекта

### Приложение api - сервис для конвертации валюты
- Вью для get-запроса и обработки параметров  
- Сериализатор для проверки параметров: наличие, соответствие    

Запрос:  
```python
http://127.0.0.1:8000/convert/?from=USD&to=RUB&amount=25000
```
  
Ответ:  
```python
{
  "query": {
    "from": "USD",
    "to": "RUB",
    "amount": 25000
   },
  "result": 2590593.3413124997
}  
```
Примеры для тестирования сервиса:  
http://127.0.0.1:8000/convert?from=USD&to=EUR&amount=100  
http://127.0.0.1:8000/convert?from=rub&to=USD&amount=100  
http://127.0.0.1:8000/convert?from=RUB&to=eur&amount=100  
http://127.0.0.1:8000/convert?from=rub&to=qqq&amount=100  
http://127.0.0.1:8000/convert?from=RUB&to=qqq&amount=100 


### freecurrencyapi сервис - сторонний сервис
Реализация в файле api/external_currency/freecurrencyapi.py  
Чтобы протестировать работу сервиса, допишите в конце файла:  
```python
if __name__ == '__main__':
    result = convert('RUB', 'EUR', 10000)
    print(result)
```
Запустите файл.

Документация на сервис - https://freecurrencyapi.com/docs/  
Для подключения нужен apikey, бесплатный тариф имеет ограничения: "5k Free Monthly Requests + 32 World Currencies + All exchange rates are updated on a daily basis".  

### Конфиг для логирования
/api/external_currency/config.py

## Развёртывание
Для локального развёртывания создан файл ...  
Для развёртывания на сервере создан файл ...  
Дописать про action CI/CD  
