# Generated by Django 3.2.2 on 2022-12-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0014_detalle_efectividad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='efectividad',
            field=models.CharField(max_length=15, verbose_name='porcentaje de efectividad'),
        ),
    ]