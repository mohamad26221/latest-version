# Generated by Django 5.0.2 on 2024-07-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_rename_roomnumber_customuser_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='img',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]