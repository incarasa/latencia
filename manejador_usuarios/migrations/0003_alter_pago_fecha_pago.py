# Generated by Django 4.2.16 on 2024-10-09 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manejador_usuarios', '0002_remove_pago_id_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
