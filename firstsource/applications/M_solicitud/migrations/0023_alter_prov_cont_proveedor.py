# Generated by Django 3.2.2 on 2021-06-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0022_auto_20210622_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prov_cont',
            name='Proveedor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]