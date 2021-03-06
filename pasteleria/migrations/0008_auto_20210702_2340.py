# Generated by Django 3.2.3 on 2021-07-03 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0007_alter_producto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('Admin', 'Es el Admin'), ('Usuario', 'Eres un simple usuario'), ('Agregar', 'Puedes agregar clientes'), ('Eliminar', 'Puedes eliminar clientes'), ('Actualizar', 'Puedes actualizar clientes'), ('Buscar', 'Puedes buscar productos'))},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': (('Admin', 'Es el Admin'), ('Usuario', 'Eres un simple usuario'), ('Agregar', 'Puedes agregar productos'), ('Eliminar', 'Puedes eliminar productos'), ('Actualizar', 'Puedes actualizar productos'), ('Buscar', 'Puedes buscar productos'))},
        ),
    ]
