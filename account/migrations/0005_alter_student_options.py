# Generated by Django 5.0.2 on 2024-07-16 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_customuser_temporary_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('view', 'Can view student based on unit number')]},
        ),
    ]