# Generated by Django 5.0.2 on 2024-07-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_customuser_year_alter_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='typeJob',
            field=models.CharField(choices=[('مشرف وحدة', 'مشرف وحدة'), ('موظف ذاتية', 'موظف ذاتية'), ('معتمد خبز', 'معتمد خبز'), ('حارس باب', 'حارس باب')], default=None, max_length=10, null=True),
        ),
    ]
