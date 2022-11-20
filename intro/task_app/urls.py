from django.urls import path

from task_app import views

app_name = 'task_app'

urlpatterns = [
    path('create/', views.task_create, name='task_create'),  # C z CRUD

    path('list/', views.task_list, name='task_list'),  # R z CRUD (widok listy)
    path('<int:id>/', views.task_detail, name='task_detail'),  # R z CRUD (widok szczegółu)

    path('<int:id>/update/', views.task_update, name='task_update'),  # U z CRUD

    path('<int:id>/delete/', views.task_delete, name='task_delete'),  # D z CRUD
]