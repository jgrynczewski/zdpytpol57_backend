from django.urls import path

from hello_app import views

urlpatterns = [
    path('welcome/', views.welcome)
]