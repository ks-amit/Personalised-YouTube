# Generated by Django 2.2 on 2020-04-26 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_migration_fix'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='id',
            new_name='videoId',
        ),
    ]