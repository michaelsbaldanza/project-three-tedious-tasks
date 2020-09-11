from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

def index(request):
    tasks_list = Task.objects.all()
    return render(request, 'index.html', { 'tasks_list': tasks_list})