# Generated by Django 3.2.3 on 2021-06-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0002_rename_rut_cliente_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='rut',
            field=models.CharField(default='', max_length=100),
        ),
    ]
