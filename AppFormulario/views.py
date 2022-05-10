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
       
        miFormulario=InscripcionFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            inscripcion=Inscripcion(charla=informacion['charla'], nombre=informacion['nombre'], profesion=informacion['profesion'], email=informacion['email'] )
            inscripcion.save()
            return render(request, "AppFormulario/inicio.html")
    else:
        miFormulario=InscripcionFormulario()

        return render(request, "AppFormulario\inscripcionFormulario.html", {'formulario':miFormulario})
    

def registro(request):
    if request.method == 'POST':

        miFormulario = RegistroFormulario(request.POST) #aquí mellega toda la información del html


        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            persona = Registro (nombre=informacion['nombre'], apellido=informacion['apellido'],
            email=informacion['email'], profesion=informacion['profesion']) 
            persona.save()
            return render(request, "AppFormulario/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

        miFormulario= RegistroFormulario() #Formulario vacio para construir el html

        return render(request, "AppFormulario/registro.html", {"formulario":miFormulario})

def encuesta(request):
    if request.method == 'POST':

        miFormulario = Encuesta(request.POST) #aquí mellega toda la información del html


        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            pregunta = Encuesta (pregunta1=informacion['pregunta1'], pregunta2=informacion['pregunta2'],
            pregunta3=informacion['pregunta3'], pregunta4=informacion['pregunta4']) 
            pregunta.save()
            return render(request, "AppFormulario/encuesta.html") #Vuelvo al inicio o a donde quieran

    else: 

        miFormulario= Encuesta() #Formulario vacio para construir el html

        return render(request, "AppFormulario/encuesta.html", {"formulario":miFormulario})

