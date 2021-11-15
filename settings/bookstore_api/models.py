from django.db import models
from django.db.models import Count

import datetime


class Publisher(models.Model):

    name = models.CharField(max_length=500)
    description = models.TextField()

    def books_total(self):
        return Book.objects.filter(publisher=self.id).count()

    def new_books(self):
        return Book.objects.filter(publisher__id=self.id).order_by("-publish_at")[:5]

    def hot_books(self):
        return Book.objects.filter(publisher__id=self.id).order_by("-total_views")[:5]


class Author(models.Model):
    first_name = models.CharField(max_length=500, default='Unknown')
    last_name = models.CharField(max_length=500, blank=True)
    second_name = models.CharField(max_length=500, blank=True)

    def books_total(self):
        return Book.objects.filter(authors__id=self.id).count()

    def new_books(self):
        t1 = datetime.date.today() - datetime.timedelta(days=180)
        t2 = datetime.date.today()
        return Book.objects.filter(
            authors__id=self.id, publish_at__range=[t1, t2]
            ).order_by('-publish_at')[:5]

    def hot_books(self):
        return Book.objects.filter(authors__id=self.id
            ).order_by('-total_sells')[:5]


class Book(models.Model):
    title = models.CharField(max_length=500)
    annotation = models.TextField()
    isbn = models.CharField(default="0000000000000", max_length=500)
    publish_at = models.DateField(default="2021-11-15")
    total_sells = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)
    authors = models.ManyToManyField(Author,
                                     blank=True, null=True)
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  blank=True, null=True)
