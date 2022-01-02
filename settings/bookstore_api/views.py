# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from .serializers import Edit_BookSerializer
from .serializers import ShortBookSerializer

from .models import Publisher
from .serializers import PublisherSerializer
from .serializers import Edit_PublisherSerializer
from .serializers import Short2PublisherSerializer

from .models import Author
from .serializers import AuthorSerializer
from .serializers import Edit_AuthorSerializer
from .serializers import Short2AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('-id')
    serializer_class = PublisherSerializer
    http_method_names = ['get']


class Edit_PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('-id')
    serializer_class = Edit_PublisherSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('-id')
    serializer_class = AuthorSerializer
    http_method_names = ['get']


class Edit_AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('-id')
    serializer_class = Edit_AuthorSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
    http_method_names = ['get']


class Edit_BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = Edit_BookSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


@api_view(['get'])
def list_publishers(request, page, size):
    publishers = Publisher.objects.all().order_by('id')
    total = publishers.count()
    i = total - (page * size)
    if i < 0:
        i = 0
    k = i + size
    serializer = Short2PublisherSerializer(publishers, many=True).data[i:k][::-1]
    return Response({
        'items': serializer,
        'total': total,
        'page': page,
        'size': size
    })


@api_view(['get'])
def list_authors(request, page, size):
    authors = Author.objects.all().order_by('id')
    total = authors.count()
    i = total - (page * size)
    if i < 0:
        i = 0
    k = i + size
    serializer = Short2AuthorSerializer(authors, many=True).data[i:k][::-1]
    return Response({
        'items': serializer,
        'total': total,
        'page': page,
        'size': size
    })


@api_view(['get'])
def list_books(request, page, size):
    books = Book.objects.all().order_by('id')
    total = books.count()
    i = total - (page * size)
    i = 0 if i < 0 else i
    k = i + size
    serializer = ShortBookSerializer(books, many=True).data[i:k][::-1]
    return Response({
        'items': serializer,
        'total': total,
        'page': page,
        'size': size
    })
