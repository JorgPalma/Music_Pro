# Generated by Django 4.0.4 on 2022-05-19 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_producto_valor_ofera_producto_valor_oferta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='valor_oferTa',
            new_name='valor_oferta',
        ),
    ]
