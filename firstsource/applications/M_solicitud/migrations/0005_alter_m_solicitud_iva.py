# Generated by Django 3.2.2 on 2021-06-14 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M_solicitud', '0004_auto_20210613_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_solicitud',
            name='iva',
            field=models.DecimalField(decimal_places=0, max_digits=12),
        ),
    ]