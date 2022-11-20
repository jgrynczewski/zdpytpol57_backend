from django.urls import path

from form_app0 import views

app_name = 'form_app0'

urlpatterns = [
    path('', views.create_task, name='create_task'),
    path('task-list/', views.task_list, name='task_list'),
]
