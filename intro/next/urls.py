from django.urls import path

from next import views


urlpatterns = [
    path('hello/', views.hello),
    path('hello2/', views.hello2),
    path('isitnewyear/', views.is_it_new_year),
    path('fruits/', views.fruits),

    path('<str:name>/', views.name_view),
]