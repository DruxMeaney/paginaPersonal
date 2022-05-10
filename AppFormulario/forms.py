from django import forms


class InscripcionFormulario(forms.Form):
    charla= forms.IntegerField()
    nombre= forms.CharField(max_length=50)
    profesion= forms.CharField(max_length=30)
    email= forms.EmailField()

    #Especificar los campos
 ##    camada = forms.IntegerField()


class RegistroFormulario(forms.Form):   
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)

class Encuesta(forms.Form):   
    pregunta1= forms.CharField(max_length=50)
    pregunta2= forms.CharField(max_length=50)
    pregunta3= forms.CharField(max_length=50)
    pregunta4= forms.CharField(max_length=50)