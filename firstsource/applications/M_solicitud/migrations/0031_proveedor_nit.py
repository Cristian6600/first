# Generated by Django 3.2.2 on 2021-06-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0030_auto_20210624_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='Nit',
            field=models.CharField(default=1, max_length=12, unique=True),
            preserve_default=False,
        ),
    ]