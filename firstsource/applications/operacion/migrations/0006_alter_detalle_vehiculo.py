# Generated by Django 3.2.2 on 2022-12-06 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0005_alter_detalle_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='vehiculo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operacion.facturacion', verbose_name='id_vehiculo'),
        ),
    ]
