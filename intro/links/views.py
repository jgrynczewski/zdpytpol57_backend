from django.shortcuts import render


# Create your views here.
def first(request):
    return render(
        request,
        'first.html',
    )


def second(request):
    return render(
        request,
        'second.html'
    )


def third(request, param):
    return render(
        request,
        'third.html',
        context={
            'param': param
        }
    )
