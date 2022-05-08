from re import template
from django.http import HttpResponse
import datetime
from django.shortcuts import render
#import Context
from django.template import  loader

#def inicio(request):
 #   return render(request, "Plantillas/template.html")

def template1(self):
    
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render()
    return HttpResponse(documento)

def template2(self):
    
    plantilla=loader.get_template("template2.html")
    documento=plantilla.render()
    return HttpResponse(documento)