from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Task,Category, Place



def index(request):
    latest_task_list = Task.objects.order_by('-pub_date')
    category_list = Category.objects.all()
    place_list = Place.objects.all()
    template = loader.get_template('tasks/index.html')
    context = {
        'latest_task_list': latest_task_list,
        'category_list': category_list,
        'place_list': place_list,
    }
    return HttpResponse(template.render(context, request))

# def detail(request, task_id):
#     try:
#         task = Task.objects.get(pk=task_id)
#     except Task.DoesNotExist:
#         raise Http404("Task does not exist")
#     return render(request, 'tasks/detail.html', {'task': task})
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

def results(request, task_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % task_id)

def vote(request, task_id):
    return HttpResponse("You're voting on question %s." % task_id)