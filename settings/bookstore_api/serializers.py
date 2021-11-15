from rest_framework import serializers

from .models import Book
from .models import Publisher
from .models import Author


class ShortBookSerializer(serializers.ModelSerializer):
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


class PublisherSerializer(serializers.ModelSerializer):
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


class Edit_PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = (
            'id',
            'name',
            'description',
        )


class AuthorSerializer(serializers.ModelSerializer):
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


class Edit_AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'second_name',
        )


class ShortPublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = (
            'id',
            'name'
        )


class Short2PublisherSerializer(serializers.ModelSerializer):
    '''use in publishers_list'''
    class Meta:
        model = Publisher
        fields = (
            'id',
            'name',
            'books_total'
        )


class ShortAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'second_name'
        )

class Short2AuthorSerializer(serializers.ModelSerializer):
    '''use in authors_list'''
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'second_name',
            'books_total',
        )


class BookSerializer(serializers.ModelSerializer):
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


class Edit_BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Author.objects.all())
    
    publisher = serializers.PrimaryKeyRelatedField( 
        queryset=Publisher.objects.all())

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
