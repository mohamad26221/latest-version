# Generated by Django 5.0.2 on 2024-05-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_customuser_city_customuser_faculty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Unites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unites', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Univesities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
