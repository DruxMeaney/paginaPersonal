from django.http import HttpResponse
from django.shortcuts import render
from .models import *
#from django.template import httpResponse

# Create your views here.
def curso(self):
    curso=Curso(nombre="Curso de Django", comision=1234)
    curso.save()
    texto = f"Curso: {curso.nombre} comisión: {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request, "AppFormulario\inicio.html")

def inscripcion(request):
    return render(request, "AppFormulario\inscripcion.html")
    #return HttpResponse("Aquí estás tú chelmo")

def profesores(request):
    return HttpResponse("Esta es la página de profesores")

def estudiantes(request):
    return HttpResponse("Esta es la página de estudiantes")

def cursos(request):
    return HttpResponse("Esta es la página de cursos")

def entregables(request):
    return HttpResponse("Esta es la página de entregables")
