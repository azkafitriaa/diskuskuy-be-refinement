# Generated by Django 3.2.18 on 2023-05-04 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0013_initialpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='nestedreplypost',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nested_reply_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='replypost',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reply_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
