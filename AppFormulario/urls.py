from django.urls import path
from .views import *

urlpatterns = [
 path('', inicio, name='inicio'),
 path('registro/', registro, name='registro'),
 path('encuesta/', encuesta, name='encuesta'),
 path('inscripcionFormulario/', inscripcionFormulario, name='inscripcionFormulario'),
    
]





