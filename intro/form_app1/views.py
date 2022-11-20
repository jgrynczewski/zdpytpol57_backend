from django.shortcuts import render

TASKS = []


def create_task(request):
    task = request.GET.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'form_app1/create_task.html',
        context={
            'tasks': TASKS
        }
    )
