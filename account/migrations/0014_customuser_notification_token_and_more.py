# Generated by Django 5.0.7 on 2024-08-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_remove_registrationrequest_attachments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='notification_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='notification_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
