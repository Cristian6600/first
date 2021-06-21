# Generated by Django 3.2.2 on 2021-06-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0010_alter_seguridad_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(verbose_name=models.Model)),
                ('Cta', models.IntegerField()),
                ('D_C', models.CharField(max_length=2)),
                ('Identificacion', models.CharField(max_length=15)),
                ('Nombre', models.CharField(max_length=70)),
                ('Codigo', models.CharField(max_length=8)),
                ('Nombre_CC', models.CharField(max_length=20)),
                ('Concepto', models.CharField(max_length=40)),
                ('Valor', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Nomina ',
                'verbose_name_plural': 'Nomina',
            },
        ),
        migrations.DeleteModel(
            name='Cargue',
        ),
        migrations.AlterModelOptions(
            name='seguridad',
            options={'verbose_name': 'Seguridad Social y Prestaciones', 'verbose_name_plural': 'Seguridad Social y Prestaciones'},
        ),
    ]
