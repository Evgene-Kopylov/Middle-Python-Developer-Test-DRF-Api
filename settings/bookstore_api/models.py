from django.db import models
from django.db.models import Count

import datetime


class Publisher(models.Model):

    name = models.CharField(max_length=500)
    description = models.TextField()

    def books_total(self):
        return Book.objects.filter(publisher=self.id).count()

    def new_books(self):
        return Book.objects.filter(publisher__id=self.id
            ).order_by("-publish_at"
            ).values(
            'id', 'title', 'annotation', 'publish_at', 'total_sells', 'total_views'
            )[:5]

    def hot_books(self):
        return Book.objects.filter(publisher__id=self.id
            ).order_by("-total_views").values(
            'id', 'title', 'annotation', 'publish_at', 'total_sells', 'total_views'
            )[:5]


class Author(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500, blank=True)
    second_name = models.CharField(max_length=500, blank=True)

    def books_total(self):
        return Book.objects.filter(authors__id=self.id).count()

    def new_books(self):
        books = Book.objects.filter(authors__id=self.id
            ).filter(publish_at__range=
            [datetime.date.today() - datetime.timedelta(days=180),
            datetime.date.today()]).order_by('publish_at')[::-1][:5]
        return [{
            'id':b.id,
            'title':b.title,
            'annotation':b.annotation,
            'publish_at':b.publish_at,
            'total_sells':b.total_sells,
            'total_views':b.total_views
            } for b in books]

    def hot_books(self):
        books = Book.objects.filter(authors__id=self.id
            ).order_by('total_sells')[::-1][:5]
        return [{
            'id':b.id,
            'title':b.title,
            'annotation':b.annotation,
            'publish_at':b.publish_at,
            'total_sells':b.total_sells,
            'total_views':b.total_views
            } for b in books]


class Book(models.Model):

    title = models.CharField(max_length=500)
    annotation = models.TextField()
    isbn = models.CharField(default="9783161484100", max_length=500)
    # input_formats=['%Y-%m-%d']
    publish_at = models.DateField(default=datetime.date.today())
    total_sells = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)
    authors = models.ManyToManyField(Author,
                                     blank=True, null=True)
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  blank=True, null=True)
