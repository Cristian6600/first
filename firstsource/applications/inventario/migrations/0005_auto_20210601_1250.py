# Generated by Django 3.2.2 on 2021-06-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20210601_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='Bloq_ex',
            field=models.BooleanField(blank=True, default=False, verbose_name='Bloqueo de extraibles'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='bloq_pa',
            field=models.BooleanField(blank=True, default=False, verbose_name='Bloqueo de panel de control'),
        ),
    ]
