# Generated by Django 3.2.18 on 2023-05-04 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20230315_1405'),
        ('post', '0018_auto_20230504_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialpost',
            name='thread',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initial_post', to='forum.thread'),
        ),
        migrations.AlterField(
            model_name='nestedreplypost',
            name='reply_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nested_reply_post', to='post.replypost'),
        ),
        migrations.AlterField(
            model_name='replypost',
            name='initial_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_post', to='post.initialpost'),
        ),
    ]
