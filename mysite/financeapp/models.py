from django.db import models

class FinancialAsset(models.Model):
    name_text = models.CharField(max_length=200)
    task_descr = models.CharField(max_length=900, default='Нет описания')
    investment_date = models.DateTimeField('Investment date')
    # task_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name_text
