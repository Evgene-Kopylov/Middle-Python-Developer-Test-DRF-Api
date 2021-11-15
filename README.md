# MYFI-Middle-Python-Developer-Test


## Запуск

В дирректории проекта Middle-Python-Developer-Test-DRF-Api перейти в settings и запустить проект 

```console
cd settings
docker-compose up
```
---
Генерировать данные в базу. 
```console
python manage.py generate_content
```
---

Swaggler 
http://127.0.0.1:8000/
/list_books/{page}/{size}/       GET список элементов страницами 
/items/book/{id}/                GET отдельный элемент
/items/edit_book/                POST
/items/edit_book/{id}/           PATCH, DELETE

