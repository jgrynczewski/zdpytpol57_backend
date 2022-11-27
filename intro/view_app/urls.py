from django.urls import path
from django.views.generic import TemplateView

from view_app import views

app_name = 'view_app'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.Hello.as_view(), name='hello2'),

    path('template/hello/', views.template_hello, name='template_hello'),
    path('template/hello2/', views.HelloView.as_view(), name='template_hello2'),
    path('template/hello3/', views.HelloGenericView.as_view(), name='template_hello3'),
    path('template/hello4/', views.TemplateView.as_view(template_name='view_app/hello.html'), name='template_hello4'),

    path('template2/hello/', views.template_hello2, name='template2_hello'),
    path('template2/hello2/', views.HelloClassView2.as_view(), name='template2_hello2'),
    path('template2/hello3/', views.HelloGenericView2.as_view(), name='template2_hello3'),

    path('person/<int:id>/', views.person_detail, name='person_detail'),
    path('person2/<int:id>/', views.PersonView.as_view(), name='person_detail2'),
    path('person3/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail3'),

    path('create-person/', views.create_person, name='create_person'),
    path('create-person2/', views.PersonCreateView.as_view(), name='create_person2'),
    path('create-person3/', views.PersonGenericCreateView.as_view(), name='create_person3'),

]
