# Generated by Django 3.1.5 on 2021-01-23 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_auto_20210123_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='place',
            new_name='places',
        ),
    ]