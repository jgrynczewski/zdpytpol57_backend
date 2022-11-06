from django.urls import path

from next import views


urlpatterns = [
    path('hello/', views.hello),
    path('hello2/', views.hello2),
]