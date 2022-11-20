from django.shortcuts import render, redirect

from form_app4.models import Task


def create_task(request):
    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Task.objects.create(name=task)

        return redirect('form_app4:create_task')

    elif request.method == "GET":
        tasks = Task.objects.all()

        return render(
            request,
            'form_app4/create_task.html',
            context={
                'tasks': tasks
            }
        )
