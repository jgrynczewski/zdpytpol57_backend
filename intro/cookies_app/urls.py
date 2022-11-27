from django.urls import path

from cookies_app import views

app_name = "cookies_app"

urlpatterns = [
    path('set-cookie/', views.set_cookie, name="set_cookie"),
    path('session-view/', views.session_view, name='session_view'),

    path('index/', views.index, name='index'),
]