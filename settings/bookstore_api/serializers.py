from rest_framework import serializers

from .models import Book
from .models import Publisher
from .models import Author


class ShortBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'annotation',
            'publish_at',
            'total_sells',
            'total_views'
        )


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    new_books = ShortBookSerializer(many=True)
    hot_books = ShortBookSerializer(many=True)

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
    new_books = ShortBookSerializer(many=True)
    hot_books = ShortBookSerializer(many=True)

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


class ShortPublisherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Publisher
        fields = (
            'id',
            'name'
        )


class ShortAuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'second_name'
        )


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = ShortAuthorSerializer(many=True)
    publisher = ShortPublisherSerializer()

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
