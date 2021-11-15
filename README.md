# MYFI-Middle-Python-Developer-Test


## Запуск
1. В дирректории проекта перейти в DB_Postges и запустить БД.
```bash
cd DB_Postges
docker-compose up
```

2. В дирректории проекта перейти в settings и запустить проект

```console
cd settings
docker-compose up
```

Генерировать данные в базу. 
```console
python manage.py generate_content
```


Swaggler 
http://127.0.0.1:8000/
/list_books/{page}/{size}/       GET список элементов страницами 
/items/book/{id}/                GET отдельный элемент
/items/edit_book/                POST
/items/edit_book/{id}/           PATCH, DELETE


---
Для тестов переключить в settings.py базу на ту что Django использует по умолчанию. Приложение должно иметь право создавать базу для тестов.
```code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
