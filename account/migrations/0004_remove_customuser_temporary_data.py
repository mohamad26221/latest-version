# Generated by Django 5.0.2 on 2024-07-15 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_temporary_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='temporary_data',
        ),
    ]
