from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import HttpResponse


def add_task(request):
    new_task = request.POST['task']
    Task.objects.create(task=new_task)
    return redirect('home')


def mark_done(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_undone(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk).delete()
    return redirect('home')


def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task,
        }
    return render(request, 'edit_task.html', context=context)
