# Generated by Django 3.2.2 on 2022-09-14 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0015_auto_20220914_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
