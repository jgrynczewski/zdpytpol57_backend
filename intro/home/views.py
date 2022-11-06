from markupsafe import escape

from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def hi(request):
    return HttpResponse("Hi!")


def adam(request):
    return HttpResponse("Witaj, Adam!")


def ewa(request):
    return HttpResponse("Witaj, Ewa!")


def welcome(request, name):
    escaped_name = escape(name)

    if name == 'john':
        return HttpResponse("Sorry, nie lubimy Johnych")
    else:
        return HttpResponse(f"Powitać, {escaped_name}!")
