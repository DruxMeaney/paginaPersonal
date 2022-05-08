from django.urls import path
from .views import *

urlpatterns = [
 path('', inicio),
 path('profesores/', profesores),
 path('estudiantes/', estudiantes),
 path('entregables/', entregables),
 path('inscripcion/', inscripcion),
 path('cursos/', cursos),
    
]





