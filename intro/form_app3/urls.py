from django.urls import path

from form_app3 import views

app_name = 'form_app3'

urlpatterns = [
    path('', views.create_task, name='create_task')
]
