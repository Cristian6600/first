# Generated by Django 3.2.2 on 2021-06-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0005_alter_cargue_total_descuentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargue',
            name='Total_descuentos',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
    ]
