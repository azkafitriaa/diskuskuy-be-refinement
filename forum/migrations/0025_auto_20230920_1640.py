# Generated by Django 3.2.20 on 2023-09-20 09:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autentikasi', '0006_auto_20230920_1554'),
        ('forum', '0024_alter_thread_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='autentikasi.customgroup'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 20, 16, 40, 16, 285264)),
        ),
    ]