# Generated by Django 3.2.2 on 2022-09-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0038_alter_dotacion_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='total_unidades',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
