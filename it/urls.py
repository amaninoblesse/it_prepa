"""graphe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from . import views

app_name='it'
urlpatterns = [
    path('home/', views.home,name='home'),
    path('newhome/', views.newhome,name='newhome'),
    path('newconnexion/', views.newconnexion,name='newconnexion'),
    path('about/', views.about,name='about'),
    path('blog/', views.blog,name='blog'),
    path('contact/', views.contact,name='contact'),
    path('teacher/', views.teacher,name='teacher'),
    path('courses/', views.courses,name='courses'),
    path('blog_single/', views.blog_single,name='blog_single'),




    path('register/', views.register,name='register'),
    path('success/', views.success,name='success'),
    path('fail/', views.fail,name='fail'),
    path('login/', views.login_request,name='login_request'),
    path('quiz/', views.quiz,name='quiz'),
    path('connexion/', views.connexion,name='connexion'),
    # path('logout/', views.logout,name='logout'),

     
]
