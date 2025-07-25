# Generated by Django 5.2.1 on 2025-05-09 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text="Unique city code (e.g., 'AMS', 'ANT', ...)", max_length=10, unique=True)),
                ('name', models.CharField(help_text="Name of the city (e.g., 'Amsterdam', 'Antwerp', ...)", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text="Unique hotel code (e.g., 'AMS01', 'ANT02', ...)", max_length=20, unique=True)),
                ('name', models.CharField(help_text='Full name of the hotel', max_length=255)),
                ('city', models.ForeignKey(help_text='The city where the hotel is located', on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='bestHotelApp.city')),
            ],
        ),
    ]
