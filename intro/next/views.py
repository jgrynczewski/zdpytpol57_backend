from django.shortcuts import render
from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("<!DOCTYPE html><html><body>Hello, world!</body></html>")


def hello2(request):
    return render(request, 'next/hello.html')


def name_view(request, name):
    return render(
        request,
        'next/name.html',
        context={'name': name}
    )
