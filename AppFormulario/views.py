from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
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

def inscripcionFormulario(request):

    if request.method == 'POST':
        print(request.POST)

    return render(request, "AppFormulario\inscripcionFormulario.html")
    

def registro(request):
    if request.method == 'POST':

        miFormulario = RegistroFormulario(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            persona = Registro (nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'], profesion=informacion['profesion']) 

            persona.save()

            return render(request, "AppFormulario/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

        miFormulario= RegistroFormulario() #Formulario vacio para construir el html

    return render(request, "AppFormulario/registro.html", {"miFormulario":miFormulario})

def estudiantes(request):
    return HttpResponse("Esta es la página de estudiantes")


def entregables(request):
    return HttpResponse("Esta es la página de entregables")
