from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

def index(request):
    tasks_list = Task.objects.all()
    task_form = TaskForm()
    return render(request, 'index.html', {
        'tasks_list': tasks_list,
        'task_form': task_form
        })