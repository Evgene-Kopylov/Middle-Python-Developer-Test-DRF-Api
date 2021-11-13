from django.shortcuts import render
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer

from .models import Publisher
from .serializers import PublisherSerializer

from .models import Author
from .serializers import AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')[::-1]
    serializer_class = BookSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')[::-1]
    serializer_class = AuthorSerializer
