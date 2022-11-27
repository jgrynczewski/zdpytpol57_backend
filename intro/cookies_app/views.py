from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


def set_cookie(request):
    # wyswietlenie ciasteczek
    cookies = request.COOKIES
    print(cookies)

    res = HttpResponse("OK")

    # ustawienie ciasteczka
    # res.set_cookie('vendor', 'Bosh')
    # res.set_cookie('User', 'Jan')

    # ciasteczko moze miec ustawiony czas wygasania
    # res.set_cookie('num', 10, max_age=20)

    # usuniecie ciasteczka
    # res.delete_cookie('vendor')

    return res


def session_view(request):
    counter = request.session.get('counter')
    if counter:
        counter += 1
    else:
        counter = 1

    request.session['counter'] = counter
    return HttpResponse(counter)


def index(request):

    # wyświetlanie uzytkownikow
    users = User.objects.all()
    print(users)

    # tworzenie uzytkownika
    # User.objects.create_user(username='jan', password='tajne')

    # uwierzytelnienie uzytkownika
    authenticated_user = authenticate(username='jan', password='tajne')

    # logowanie uzytkownika
    if authenticated_user:
        login(request, authenticated_user)

    # wylogowanie użytkownika
    logout(request)

    return HttpResponse(f"Witaj {request.user}")
