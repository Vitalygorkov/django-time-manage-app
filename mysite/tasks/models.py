from django.db import models

class Place(models.Model):
    place_name = models.CharField(max_length=200)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    # task_in_place = models.ManyToManyField(Task, blank=True)
    # task_in_place = models.ManyToManyField(Task, null=True, blank=True)
    def __str__(self):
        return self.place_name

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    task_descr = models.CharField(max_length=900, default='Нет описания')
    target_date = models.DateField('target date', null= True, blank=True)
    pub_date = models.DateTimeField('date published')
    task_completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    places = models.ManyToManyField(Place)



    def __str__(self):
        return self.task_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    cat_descr = models.CharField(max_length=900)
    # target_date = models.DateField('target date', null= True, blank=True)
    # pub_date = models.DateTimeField('date published')
    # task_completed = models.BooleanField(default=False)
    # parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)




    def __str__(self):
        return self.category_name


class TaskUnder(models.Model):
    taskunder = models.ForeignKey(Task, on_delete=models.CASCADE)
    taskunder_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.taskunder_text


