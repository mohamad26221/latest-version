# Generated by Django 5.0.2 on 2024-07-16 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('change_room', 'Can change room field')]},
        ),
    ]
