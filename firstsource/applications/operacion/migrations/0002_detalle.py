# Generated by Django 3.2.2 on 2022-12-06 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacion.facturacion')),
            ],
        ),
    ]
