# Generated by Django 3.1.5 on 2021-01-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_auto_20210123_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='task_in_place',
        ),
        migrations.RemoveField(
            model_name='task',
            name='place_in_task',
        ),
        migrations.AddField(
            model_name='task',
            name='place_in_task',
            field=models.ManyToManyField(to='tasks.Place'),
        ),
    ]
