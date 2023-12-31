# Generated by Django 4.2.3 on 2023-11-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0005_juegos_img_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Streamers',
            fields=[
                ('Stream_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('img_url', models.ImageField(upload_to='imgStream')),
                ('icon', models.ImageField(upload_to='icon')),
            ],
        ),
    ]
