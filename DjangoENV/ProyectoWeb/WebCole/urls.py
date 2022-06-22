from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alumno', views.gestion_alumno, name='gestion_alumno'),
    path('', views.home, name='login')
]
