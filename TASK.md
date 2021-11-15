Тестовое задание для соискателей на вакансию Python разработчика уровня Middle в финтех проект MYFI.

## Задание

Необходимо разработать REST API которое будет позволять добавлять, редактировать, просматривать и удалять записи по книгам, авторам и издателям.

API должно использовать методы:

-   GET
-   POST
-   PATCH
-   DELETE

### Издатели

На GET запрос списка издателей должен возвращаться следующий JSON ответ:

```json
{
    "items": [
        {
            "id": 1, // идентификатор издателя
            "name": "Publisher", // имя издателя
            "books_total": 100 // кол-во напечатанных книг этим издателем
        }
    ],
    "total": 1, // кол-во издателей в БД
    "page": 1, // текущая страница
    "size": 1 // кол-во издателей на 1 страницу
}
```

На GET запрос по конкретному издателю должен возвращаться следующий JSON ответ:

```json
{
    "id": 1, // идентификатор издателя
    "name": "Publisher", // имя издателя
    "description": "Bla bla bla", // описание издателя
    "books_total": 100, // кол-во напечатанных книг этим издателем
    "new_books": [ // список новых книг, не более 5 шт.
        {
            "id": 1, // идентификатор книги
            "title": "Book title", // заголовок книги
            "annotation": "Book annotation...", // краткое изложение книги
            "publish_at": "2021-02-28", // дата публикации
            "total_sells": 100, // кол-во продаж
            "total_views": 10000 // кол-во просмотров
        }
    ],
    "hot_books": [ // список самых продаваемых книг, не более 5 шт.
        {
            "id": 1, // идентификатор книги
            "title": "Book title", // заголовок книги
            "annotation": "Book annotation...", // краткое изложение книги
            "publish_at": "2021-02-28", // дата публикации
            "total_sells": 100, // кол-во продаж
            "total_views": 10000 // кол-во просмотров
        }
    ]
}
```

### Авторы

На GET запрос списка авторов должен возвращаться следующий JSON ответ:

```json
{
    "items": [
        {
            "id": 1, // идентификатор автора
            "first_name": "Александр", // имя автора
            "last_name": "Пушкин", // фамилия автора
            "second_name": "Сергеевич", // отчество автора
            "books_total": 100 // кол-во книг опубликованных книг у автора
        }
    ],
    "total": 1, // кол-во авторов в БД
    "page": 1, // текущая страница
    "size": 1 // кол-во авторов на 1 страницу
}
```

На GET запрос по конкретному автору должен возвращаться следующий JSON ответ:

```json
{
    "id": 1, // идентификатор автора
    "first_name": "Александр", // имя автора
    "last_name": "Пушкин", // фамилия автора
    "second_name": "Сергеевич", // отчество автора
    "books_total": 100, // кол-во опубликованных книг у автора
    "new_books": [ // список новых книг, не более 5 шт.
        {
            "id": 1, // идентификатор книги
            "title": "Book title", // заголовок книги
            "annotation": "Book annotation...", // краткое изложение книги
            "publish_at": "2021-02-28", // дата публикации
            "total_sells": 100, // кол-во продаж
            "total_views": 10000 // кол-во просмотров
        }
    ],
    "hot_books": [ // список самых продаваемых книг, не более 5 шт.
        {
            "id": 1, // идентификатор книги
            "title": "Book title", // заголовок книги
            "annotation": "Book annotation...", // краткое изложение книги
            "publish_at": "2021-02-28", // дата публикации
            "total_sells": 100, // кол-во продаж
            "total_views": 10000 // кол-во просмотров
        }
    ]
}
```

### Книги

На GET запрос списка книг должен возвращаться следующий JSON ответ:

```json
{
    "items": [
        {
            "id": 1, // идентификатор книги
            "title": "Book title", // заголовок книги
            "annotation": "Book annotation...", // краткое изложение книги
            "publish_at": "2021-02-28", // дата публикации
            "total_sells": 100, // кол-во продаж
            "total_views": 10000 // кол-во просмотров
        }
    ],
    "total": 1, // кол-во авторов в БД
    "page": 1, // текущая страница
    "size": 1 // кол-во авторов на 1 страницу
}
```

На GET запрос по конкретной книге должен возвращаться следующий JSON ответ:

```json
{
    "id": 1, // идентификатор книги
    "title": "Book title", // заголовок книги
    "annotation": "Book annotation..." // краткое изложение книги
    "isbn": "9783161484100",
    "publish_at": "2021-02-28", // дата публикации
    "total_sells": 100, // кол-во продаж
    "total_views": 10000, // кол-во просмотров
    "authors": [ // полный список авторов книги
        {
            "id": 1, // идентификатор автора
            "first_name": "Александр", // имя автора
            "last_name": "Пушкин", // фамилия автора
            "second_name": "Сергеевич", // отчество автора
        }
    ],
    "publisher": {
        "id": 1, // идентификатор издателя
        "name": "Publisher", // имя издателя
    }
}
```

## Требования

-   REST API должно быть написано на языке Python версии 3.7 или младше, с использованием фреймворка FastAPI.
-   Написанное приложение должно использовать БД PostgreSQL, все миграции должны быть реализованы с помощью инструмента Alembic.
-   Приложение должно собираться в Docker контейнер.
-   Приложение должно быть покрыто unit-тестами.
-   Приложение должно иметь Docker Compose манифест для локального запуска.
-   Код приложения должен быть опубликован на Github, Gitlab или Bitbucket в публичном репозитории.

## Критерии оценки

-   Время выполнения задания (3 дня максимум).
-   Код написан по стандарту PEP 8.
-   В **requirements.txt** перечислены только необходимые зависимости с указанием версий.
-   Качество покрытия тестами кода.
-   Для тестирования используется Faker.
-   Применяется MyPy для анализа кода.

## Сдача тестого задания

По завершению работы необходимо отправить ссылку на репозиторий куратору либо через мессенджер, либо на электронную почту: [a@myfi24.ru](mailto:a@myfi24.ru)