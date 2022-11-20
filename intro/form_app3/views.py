from django.shortcuts import render, redirect


def create_task(request):
    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            with open('tasks.txt', 'a+') as f:
                f.write(f"{task}\n")

        return redirect('form_app3:create_task')

    elif request.method == "GET":
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()

        return render(
            request,
            'form_app3/create_task.html',
            context={
                'tasks': tasks
            }
        )
