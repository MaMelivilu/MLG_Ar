# Generated by Django 4.2.2 on 2023-06-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
    ]