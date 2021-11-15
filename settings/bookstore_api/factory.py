from django.core.management.base import BaseCommand, CommandError

from factory.faker import faker
from faker.providers import DynamicProvider

import datetime

from bookstore_api.models import Publisher
from bookstore_api.models import Author
from bookstore_api.models import Book



class MyFactory:

    def fake_it(self, n):
        for i in range(n):
            self.fake_book()


    def fake_book(self):
        self.fake = faker.Faker('Ru_RU')
        fake = self.fake

        book = Book(
            title=fake.sentence(nb_words=3),
            annotation=fake.sentence(nb_words=15),
            isbn=fake.isbn13(),
            publish_at=fake.date_between(
                datetime.date.today() - datetime.timedelta(days=37000),
                datetime.date.today()
            ),
            total_sells=fake.pyint(0, 1000, 1),
            total_views=fake.pyint(0, 10000, 1),
        )
        book.save()

        author = self.fake_author()

        book.authors.add(author)

        if book.id % 3 == 0:
            author_2 = self.fake_author()
            book.authors.add(author_2)
        if book.id % 2 == 0:
            _id = fake.pyint(1, len(Author.objects.all()), 1)
            author_3 = Author.objects.filter(id=_id).first()
            book.authors.add(author_3)

        book.publisher = self.fake_publisher()
        book.save()

    def fake_publisher(self):
        publisher_provider = DynamicProvider(
            provider_name="publisher",
            elements=["РАН", "ЭКСМО", "Заря", "Донцова инкорпорейтед.", "РПЦ"],
        )
        fake = self.fake
        fake.add_provider(publisher_provider)

        name = fake.publisher()
        publisher = Publisher.objects.filter(name=name).first()
        if not publisher:
            publisher = Publisher(
                name=name,
                description=fake.sentence(nb_words=10)
            )
            publisher.save()
        return publisher

    def fake_author(self):
        fake = self.fake
        first_name = fake.first_name()
        last_name = fake.last_name()
        second_name = fake.middle_name()

        author = Author.objects.filter(
            first_name=first_name,
            last_name=last_name,
            second_name=second_name).first()
        if not author:
            author = Author(
                first_name=first_name,
                last_name=last_name,
                second_name=second_name)
            author.save()
        return author

