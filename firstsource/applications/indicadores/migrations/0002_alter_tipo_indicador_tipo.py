# Generated by Django 3.2.2 on 2021-06-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_indicador',
            name='Tipo',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
