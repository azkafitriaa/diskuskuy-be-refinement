# Generated by Django 3.2.20 on 2023-09-20 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_alter_thread_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 20, 13, 27, 46, 650557)),
        ),
    ]