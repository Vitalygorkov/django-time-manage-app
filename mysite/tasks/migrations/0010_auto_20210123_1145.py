# Generated by Django 3.1.5 on 2021-01-23 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20210123_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='task',
            new_name='task_in_place',
        ),
        migrations.AddField(
            model_name='task',
            name='place_in_task',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.place'),
        ),
    ]