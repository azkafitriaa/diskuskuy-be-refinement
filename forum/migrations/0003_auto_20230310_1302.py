# Generated by Django 3.2.18 on 2023-03-10 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20230310_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiryphase',
            name='discussion_guide',
        ),
        migrations.DeleteModel(
            name='DiscussionGuide',
        ),
    ]