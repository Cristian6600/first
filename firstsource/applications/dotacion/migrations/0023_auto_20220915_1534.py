# Generated by Django 3.2.2 on 2022-09-15 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dotacion', '0022_dotacion_stock_usado'),
    ]

    operations = [
        migrations.AddField(
            model_name='dotacion',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dotacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dotacion.dotacion')),
            ],
        ),
    ]
