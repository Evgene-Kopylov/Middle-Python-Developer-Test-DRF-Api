# Generated by Django 3.2.9 on 2021-11-13 00:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0005_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_at',
            field=models.DateField(default=datetime.date(2021, 11, 13)),
        ),
    ]
