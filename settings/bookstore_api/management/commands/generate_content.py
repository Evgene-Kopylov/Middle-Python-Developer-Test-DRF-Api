from django.core.management.base import BaseCommand, CommandError

from factory.faker import faker
from faker.providers import DynamicProvider

import datetime

from bookstore_api.models import Publisher
from bookstore_api.models import Author
from bookstore_api.models import Book




class Command(BaseCommand):
    help = 'Generate bookstore_api db content'

    def handle(self, *args, **options):
        # print('How many?')
        # n = int(input())
        n = 3
        for i in range(n):
            self.fake_book()

    def fake_book(self):
        self.fake = faker.Faker()
        fake = self.fake
        
        my_word_list = "Сказка Аленький цветочек - это литературное изложение Аксакова истории о Красавице и Чудовище. Любимая дочь попросила у отца-купца привезти ей Аленький цветочек, но оказалось, что самый красивый цветок рос в саду у чудовища. Отец сорвал цветочек и был вынужден отправить свою дочь жить к этому зверю. Девушка привязалась к чудовищу, своей любовью рассеяла магические чары и оказалось, что чудовище - это прекрасный принц..."
        fake.sentence(ext_word_list=my_word_list.split())


        book = Book(
            title = fake.sentence(ext_word_list=my_word_list, nb_words=5),
            annotation = fake.sentence(ext_word_list=my_word_list, nb_words=15),
            isbn = "9783161484100",
            publish_at = fake.date_between(
                datetime.date.today() - datetime.timedelta(days=37000),
                datetime.date.today()
                ),
            total_sells = fake.pyint(0,1000,1),
            total_views = fake.pyint(0,10000,1),
        )
        book.save()

        author = self.fake_author()
        
        book.authors.add(author)

        if book.id % 3 == 0:
            author_2 = self.fake_author()
            book.authors.add(author_2)

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
                name = name,
                description = fake.sentence(ext_word_list=my_word_list, nb_words=10))
            publisher.save()
        return publisher


    def fake_author(self):
        fake = self.fake
        first_name = fake.first_name()
        last_name = fake.last_name()
        second_name = fake.first_name()

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

