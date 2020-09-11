from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    tasks_list = Task.objects.all()
    task_form = TaskForm()
    print(tasks_list)
    print(task_form)
    return render(request, 'index.html', {
        'tasks_list': tasks_list,
        'task_form': task_form
        })
        
def add_task(request, task_id):
    pass