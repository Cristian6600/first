# Generated by Django 3.2.2 on 2022-12-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0013_auto_20221213_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='efectividad',
            field=models.CharField(default=1, max_length=5, verbose_name='porcentaje de efectividad'),
            preserve_default=False,
        ),
    ]
