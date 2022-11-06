from django.urls import path

from links import views

urlpatterns = [
    path('pierwszy/', views.first),
    path('second/', views.second),
]