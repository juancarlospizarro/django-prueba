from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task, Jugador

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def projects(request):
    projects = list(Project.objects.all())
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    tasks = list(Task.objects.all())
    return render(request, 'tasks.html', {'tasks': tasks})

def jugadores(request):
    return render(request, 'jugadoresAPI.html')

def lista_jugadores(request):
    jugadores = list(Jugador.objects.values())  # Convierte QuerySet en lista de diccionarios
    return JsonResponse(jugadores, safe=False)