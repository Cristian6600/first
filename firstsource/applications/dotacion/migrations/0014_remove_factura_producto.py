# Generated by Django 3.2.2 on 2022-09-14 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0013_producto_factura_factura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='producto',
        ),
    ]