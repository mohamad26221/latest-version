# Generated by Django 5.0.2 on 2024-07-16 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('مشرف وحدة', 'Can change room field')]},
        ),
    ]
