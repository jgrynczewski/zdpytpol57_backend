from django.shortcuts import render, redirect, get_object_or_404

from task_app.models import Task


# Widok tworzenia (Create - C z CRUD)
def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(name=title)

        return redirect('task_app:task_list')

    return render(
        request,
        'task_app/task_create.html'
    )


# Widok listy (Read - R z CRUD)
def task_list(request):
    tasks = Task.objects.all()

    return render(
        request,
        'task_app/task_list.html',
        context={
            'tasks': tasks,
        }
    )


# Widok detalu (Read - R z CRUD)
def task_detail(request, id):
    task = get_object_or_404(Task, id=id)

    return render(
        request,
        'task_app/task_detail.html',
        context={
            'task': task,
        }
    )


# Widok modyfikacji (Update - U z CRUD)
def task_update(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        title = request.POST.get('title')

        if title:
            task.name = title
            task.save()

        return redirect('task_app:task_list')

    return render(
        request,
        'task_app/task_update.html',
        context={
            'task': task
        }
    )


# Widok usuwanie (Delete - D z CRUD)
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.delete()

        return redirect('task_app:task_list')

    return render(
        request,
        'task_app/task_confirm_delete.html',
        context={
            'task': task,
        }
    )
