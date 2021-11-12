from django.db import models

import datetime

# Create your models here.


class Publisher(models.Model):

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
