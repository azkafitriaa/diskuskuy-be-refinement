# Generated by Django 3.2.18 on 2023-04-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentikasi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'student'), ('lecturer', 'lecturer')], max_length=8),
        ),
    ]
