from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hello),
    path('projects', views.projects),
    path('tasks', views.tasks),
    path('api/jugadores', views.lista_jugadores),
    path('jugadores', views.jugadores)
]