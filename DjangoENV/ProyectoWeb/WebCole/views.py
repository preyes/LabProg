from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'WebCole/home.html')

def login(request):
    return render(request,'WebCole/login.html')

def gestion_alumno(request):
    return render(request,'WebCole/alumnos.html')