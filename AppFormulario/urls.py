from django.urls import path
from .views import *

urlpatterns = [
 path('', inicio, name='inicio'),
 path('registro/', registro, name='registro'),
 path('estudiantes/', estudiantes),
 path('entregables/', entregables),
 path('inscripcion/', inscripcion, name='inscripcion'),
 path('inscripcionFormulario/', inscripcionFormulario, name='inscripcionFormulario'),
    
]





