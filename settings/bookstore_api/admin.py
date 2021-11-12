from django.contrib import admin

from .models import Publisher
from .models import Author
from .models import Book

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)


