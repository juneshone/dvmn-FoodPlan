# dvmn-FoodPlan
FoodPlan - это онлайн-сервис с платной подпиской на рецепты, который поможет вам спланировать свой рацион, расходы на питание и выбрать блюда для специальной диеты.

[Ссылка на сайт](https://ozhiv.pythonanywhere.com/)

## Подготовка к запуску проекта
 
1. Python версии 3.9 или 3.10 должен быть уже установлен. Склонируйте репозиторий и создайте виртуальную среду командой:

```python
python -m venv venv
```

2. Активируйте виртуальную среду для Windows:

```python
.\venv\Scripts\activate.bat
```
для Linux:

```python
source venv/bin/activate
```

3. Затем используйте pip для установки зависимостей:

```python
pip install -r requirements.txt
```

## Переменнные окружения

Часть данных проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` и присвойте значения переменным окружения в формате: ПЕРЕМЕННАЯ=значение.

_Переменные окружения проекта:_

```ini
ALLOWED_HOSTS='host1,host2'                 # белый список хостов
DJANGO_DEBUG=True                           # отладочный режим
DJANGO_SECRET_KEY='django_secret_key'       # секретный ключ django проекта
```

## Как запустить

1. Создайте базу данных SQLlite:
    
```python
python manage.py migrate
```
    
2. Создайте суперпользователя для доступа в Django-админку:

```python
python manage.py createsuperuser
```

3. Наполните базу данных через админ-интерфейс.

4. Запустите сервер Django:
    
```python
python manage.py runserver 0:8000
```
    
Админ-интерфейс будет доступен по адресу `127.0.0.1:8000/admin`.
Для доступа используйте логин и пароль, созданный в п.2.
