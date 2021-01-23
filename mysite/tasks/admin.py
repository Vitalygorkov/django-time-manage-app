from django.contrib import admin
from  .models import Task, Place, Category

admin.site.register(Task)
admin.site.register(Place)
admin.site.register(Category)