# Generated by Django 3.1.5 on 2021-01-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20210122_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='target_date',
            field=models.DateField(blank=True, null=True, verbose_name='target date'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_completed',
            field=models.BooleanField(default=False),
        ),
    ]
