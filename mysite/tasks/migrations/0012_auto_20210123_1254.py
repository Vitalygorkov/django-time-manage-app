# Generated by Django 3.1.5 on 2021-01-23 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20210123_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='task_in_place',
        ),
        migrations.AddField(
            model_name='place',
            name='task_in_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
