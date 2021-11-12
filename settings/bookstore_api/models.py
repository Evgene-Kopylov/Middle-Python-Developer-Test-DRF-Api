from django.db import models

import datetime

# Create your models here.
class Publisher(models.Model):
    '''
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
    '''

    name = models.CharField(max_length=500)
    description = models.TextField()

    def op(self):
        return 99999999

    def books_total(self):
        return Book.objects.filter(publisher=self.id).count()

    def new_books(self):
        return Book.objects.all().order_by("publish_at")


    def hot_books(self):
        return Book.objects.all().order_by("total_views")



class Author(models.Model):
    '''
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

    '''
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500, blank=True)
    second_name = models.CharField(max_length=500, blank=True)

    def books_total(self):
        pass

    def new_books(self):
        pass

    def hot_books(self):
        pass

class Book(models.Model):
    '''
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
    '''
    title = models.CharField(max_length=500)
    annotation = models.TextField()
    isbn = models.CharField(default="9783161484100", max_length=500)
    publish_at = models.DateField(default=datetime.date.today()) #input_formats=['%Y-%m-%d']
    total_sells = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)
    authors = models.ManyToManyField(Author,
        blank=True, null=True)
    publisher = models.ForeignKey(Publisher, 
        on_delete=models.CASCADE, 
        blank=True, null=True)