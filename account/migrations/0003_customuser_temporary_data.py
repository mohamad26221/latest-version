# Generated by Django 5.0.2 on 2024-07-15 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_email_verification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='temporary_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]