# Generated by Django 2.2 on 2020-04-26 17:41

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_migration_fix'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='video',
            name='data_video_searchV_29ddef_gin',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='searchVector',
            new_name='searchvector',
        ),
        migrations.AddIndex(
            model_name='video',
            index=django.contrib.postgres.indexes.GinIndex(fields=['searchvector'], name='data_video_searchv_975a5c_gin'),
        ),
    ]
