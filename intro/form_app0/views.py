from django.shortcuts import render

TASKS = []


def create_task(request):
    return render(
        request,
        'form_app0/create_task.html'
    )


def task_list(request):
    task = request.GET.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'form_app0/task_list.html',
        context={
            'tasks': TASKS
        }
    )
