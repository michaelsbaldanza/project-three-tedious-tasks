from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    task_list = Task.objects.all()
    task_form = TaskForm()
    print(task_list)
    print(task_form)
    return render(request, 'index.html', {'task_list': task_list, 'task_form': task_form})

def add_task(request):
  form = TaskForm(request.POST)
  if form.is_valid():
    new_task = form.save(commit=False)
    new_task.save()
  return redirect('index')