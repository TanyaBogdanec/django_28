from django.shortcuts import render
from .models import Task


def view_task(request):
    tasks = Task.objects.order_by('-date_creation')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)