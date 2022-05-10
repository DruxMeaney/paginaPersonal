from django.db import models

# Create your models here.
class Inscripcion(models.Model):
    charla= models.IntegerField()
    nombre= models.CharField(max_length=50)
    profesion= models.CharField(max_length=30)
    email= models.EmailField()
    def __str__(self):
        return self.nombre+" "+str(self.charla)



class Registro(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre+" "+str(self.apellido)

class Encuesta(models.Model):   
    pregunta1= models.CharField(max_length=50)
    pregunta2= models.CharField(max_length=50)
    pregunta3= models.CharField(max_length=50)
    pregunta4= models.CharField(max_length=50)