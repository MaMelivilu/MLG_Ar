# Generated by Django 4.2.3 on 2023-11-26 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0006_streamers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]