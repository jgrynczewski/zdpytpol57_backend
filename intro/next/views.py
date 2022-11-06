import datetime

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


def is_it_new_year(request):
    is_new_year = False
    today = datetime.date.today()
    if today.day == 6 and today.month == 11:
        is_new_year = True

    return render(
        request,
        'next/new_year.html',
        context={'is_new_year': is_new_year}
    )
