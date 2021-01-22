from django.db import models


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    task_descr = models.CharField(max_length=900, null= True, blank=True)
    pub_date = models.DateTimeField('date published')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

                                        # on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.task_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Place(models.Model):
    place = models.CharField(max_length=200)

class TaskUnder(models.Model):
    taskunder = models.ForeignKey(Task, on_delete=models.CASCADE)
    taskunder_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.taskunder_text


