from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def hi(request):
    return HttpResponse("Hi!")


