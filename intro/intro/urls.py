"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from intro.views import hello, welcome
from home.views import hi, adam, ewa, welcome


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('witaj/', welcome),
    path('hi/', hi),
    path('adam/', adam),
    path('ewa/', ewa),
    path('welcome/<str:name>/', welcome),

    path('next/', include('next.urls')),
    path('hello/', include('hello_app.urls')),
    path('links/', include('links.urls')),
    path('inheritance/', include('inheritance.urls')),
    path('form0/', include('form_app0.urls')),
    path('form1/', include('form_app1.urls')),
    path('form2/', include('form_app2.urls')),
    path('form3/', include('form_app3.urls')),
    path('form4/', include('form_app4.urls')),
    path('task/', include('task_app.urls')),
    path('relations/', include('relations.urls')),
    path('form5/', include('form_app5.urls')),
    path('view/', include('view_app.urls')),
    path('cookie/', include('cookies_app.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
]
