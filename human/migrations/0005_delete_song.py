# Generated by Django 3.2 on 2021-12-12 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0004_rename_favourite_quotes_favouritequotes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Song',
        ),
    ]
