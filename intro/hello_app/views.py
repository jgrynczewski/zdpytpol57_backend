from django.shortcuts import render


def welcome(request):
    return render(
        request,
        'hello_app/welcome.html'
    )
