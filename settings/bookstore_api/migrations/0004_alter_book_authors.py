# Generated by Django 3.2.9 on 2021-11-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0003_auto_20211112_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, to='bookstore_api.Author'),
        ),
    ]
