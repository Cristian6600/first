# Generated by Django 3.2.2 on 2021-06-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_auto_20210601_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='in_cont',
            field=models.CharField(blank=True, max_length=2, verbose_name='Intento contraseñas'),
        ),
    ]
