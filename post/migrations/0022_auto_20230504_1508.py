# Generated by Django 3.2.18 on 2023-05-04 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20230504_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialpost',
            name='post',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='initial_post', to='post.post'),
        ),
        migrations.AlterField(
            model_name='nestedreplypost',
            name='post',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='nested_reply_post', to='post.post'),
        ),
        migrations.AlterField(
            model_name='replypost',
            name='post',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reply_post', to='post.post'),
        ),
    ]