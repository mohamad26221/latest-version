# Generated by Django 5.0.7 on 2024-08-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_customuser_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationrequest',
            name='payment_method',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]