from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response



from .models import Book
from .serializers import BookSerializer
from .serializers import ShortBookSerializer

from .models import Publisher
from .serializers import PublisherSerializer
from .serializers import Short2PublisherSerializer

from .models import Author
from .serializers import AuthorSerializer
from .serializers import Short2AuthorSerializer



class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('-id')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer


@api_view()
def publishers_info(request, page, size):
    publishers = Publisher.objects.all().order_by('id')
    total = publishers.count()
    i = total - (page * size)
    if i < 0: i = 0
    k = i + size
    serializer = Short2PublisherSerializer(publishers, many=True).data[i:k][::-1]
    return Response({
        'items': serializer,
        'total': total,
        'page': page,
        'size': size
        })


@api_view()
def authors_info(request, page, size):
    authors = Author.objects.all().order_by('id')
    total = authors.count()
    i = total - (page * size)
    if i < 0: i = 0
    k = i + size
    serializer = Short2AuthorSerializer(authors, many=True).data[i:k][::-1]
    return Response({
        'items': serializer,
        'total': total,
        'page': page,
        'size': size
        })


@api_view()
def books_info(request, page, size):
    books = Book.objects.all().order_by('id')
    total = books.count()
    i = total - (page * size)
    if i < 0: i = 0
    k = i + size
    serializer = ShortBookSerializer(books, many=True).data[i:k][::-1]
    return Response({
        'items': serializer,
        'total': total,
        'page': page,
        'size': size
        })

