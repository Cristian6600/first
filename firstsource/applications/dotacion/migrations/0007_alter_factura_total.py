# Generated by Django 3.2.2 on 2022-09-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0006_dotacion_promedio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='total',
            field=models.IntegerField(blank=True),
        ),
    ]
