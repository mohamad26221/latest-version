# Generated by Django 5.0.2 on 2024-03-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_rename_user_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='faculty',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='fathername',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='idNationalNumber',
            field=models.IntegerField(default=None, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='idNumber',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='job',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mothername',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='roomNumber',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='section',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='typejob',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='unitNumber',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='university',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='year',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
