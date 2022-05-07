from re import template
from django.http import HttpResponse
import datetime
#import Context
from django.template import Context, Template, loader



def fingon(self):
    
    nom="Fingon hijo de Fingolfin"
    edad="1"
    operacion=str(datetime.datetime.now().year-int(825))
    fecha=str(operacion)
    diccionario={'nombre':nom, 'edad':edad, 'fechas':fecha}
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def galadriel(self):
    
    nom="Galadriel hija de Finarfin"
    edad="1, 2, y 3"
    fecha="-"
    diccionario={'nombre':nom, 'edad':edad, 'fechas':fecha}
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
 
def feanor(self):

     nom="Feanor hijo de Finwê"
     edad="1"
     fecha=str(datetime.datetime.now().year-int(1456))
     diccionario={'nombre':nom, 'edad':edad, 'fechas':fecha}
     plantilla=loader.get_template("template1.html")
     documento=plantilla.render(diccionario)
     return HttpResponse(documento)