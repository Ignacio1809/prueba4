# Generated by Django 3.2.3 on 2021-07-01 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0005_cliente_rut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(default='', max_length=100)),
                ('precio', models.IntegerField(default=0)),
                ('descripcion', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
