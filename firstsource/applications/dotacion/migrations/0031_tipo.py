# Generated by Django 3.2.2 on 2022-09-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0030_alter_factura_total_factura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=35)),
            ],
        ),
    ]
