from rest_framework import serializers

from .models import Book
from .models import Publisher
from .models import Author


class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Publisher
        fields = (
            'id',
            'name',
            'description',
            'books_total',
            'new_books',
            'hot_books',
        )


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'second_name',
            'books_total',
            'new_books',
            'hot_books'
        )


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True)
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'annotation',
            'isbn',
            'publish_at',
            'total_sells',
            'total_views',
            'authors',
            'publisher'
        )
