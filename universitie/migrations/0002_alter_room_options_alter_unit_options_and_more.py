# Generated by Django 5.0.7 on 2024-07-18 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universitie', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': 'الغرف'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name_plural': 'الوحدات'},
        ),
        migrations.AlterModelOptions(
            name='universitie',
            options={'verbose_name_plural': 'الجامعات'},
        ),
    ]
