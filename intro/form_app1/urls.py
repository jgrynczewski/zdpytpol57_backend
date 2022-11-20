from django.urls import path

from form_app1 import views

app_name = 'form_app1'

urlpatterns = [
    path('', views.create_task, name='create_task')
]
