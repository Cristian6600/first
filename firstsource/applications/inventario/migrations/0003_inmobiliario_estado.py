# Generated by Django 3.2.2 on 2022-12-16 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmobiliario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
