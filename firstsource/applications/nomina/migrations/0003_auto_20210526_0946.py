# Generated by Django 3.2.2 on 2021-05-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0002_alter_cargue_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargue',
            name='Cuenta_Contable',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cargue',
            name='Fecha',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cargue',
            name='Identificacion',
            field=models.IntegerField(max_length=14),
        ),
        migrations.AlterField(
            model_name='cargue',
            name='Valor',
            field=models.IntegerField(max_length=10),
        ),
    ]
