from django.urls import path

from form_app4 import views

app_name = 'form_app4'

urlpatterns = [
    path('', views.create_task, name='create_task')
]
