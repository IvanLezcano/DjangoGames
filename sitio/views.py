import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


#clase de prueba

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido




def principal(request):

    p1=Persona("juan","diaz")


    fecha_actual=datetime.datetime.now()
    nombre="ivan"
    #forma de cargar plantillas manual
    #doc_externo=open("/home/ivan/Descargas/prueba/sitio/plantillas/saludoHome.html")

    #plt=Template(doc_externo.read())

    #doc_externo.close()
    
    #doc_externo=loader.get_template("saludoHome.html")


    generosGenerales = ["rock","pop"]

    #ctx=Context({"nombre_persona":nombre, "numero_pi":314, "fecha":fecha_actual, "nombreObjeto":p1.nombre,"apellidoObjbeto":p1.apellido,"generos":["rock","pop"],"listita":generosGenerales})
      #tambien podria colocar el valor que quiero directamente
      #podes aislar los temas a una variable de lista


    #antes renderizaba el plt pero ahora deberia renderizar el doc_externo del loader
    #documento=plt.render(ctx)

    #este render esta trabajando con un template de clase distinta asique en vez de pasarle el contexto
    #podemos pasarle TOdoo lo que tenia elcontexto directamente
    
    #documento=doc_externo.render({"nombre_persona":nombre, "numero_pi":314, "fecha":fecha_actual, "nombreObjeto":p1.nombre,"apellidoObjbeto":p1.apellido,"generos":["rock","pop"],"listita":generosGenerales})

    #return HttpResponse(documento)

    #al usar render podemos prescindir de llamar al loader.get y al render pero es obligatorio
    #pasar el request, la plantilla y el contexto y tener configurado el setting de directorios
    return render(request,"saludoHome.html",{"nombre_persona":nombre, "numero_pi":314, "fecha":fecha_actual, "nombreObjeto":p1.nombre,"apellidoObjbeto":p1.apellido,"generos":["rock","pop"],"listita":generosGenerales})


def egg(request):

    return HttpResponse("easterEgg")


def tiempoActual(request):
    fecha_actual=datetime.datetime.now()
    documento="""
    <html>
    <body>
    <h1>
    Fecha y horas actuales actualizadas %s
    </h1>
    </body>
    </html> 
     """ % fecha_actual

    return HttpResponse(documento)

def procesoDeBinarioADecimal(numero,indice):
    return 2**indice*numero
"""descartado"""

def calculadorBin(request,numero):
    
    pepe = lambda x: int(x[1]) * (2 ** x[0]) 
    
    caracteresNumeros = str(numero)
    numeroBinarioDescompuesto = list(map(int,caracteresNumeros))
    numeroBinarioAlReves = enumerate(reversed(numeroBinarioDescompuesto))
    numeroDecimalTransformado = sum(map(pepe,numeroBinarioAlReves))
    

    documento="""
    <html>
    <body>
    <h2>
    Bip bip bop! el numero %s en decimal seria este %s 
    Whoshhhh
    </h2>
    </body>
    </html> 
     """ %(numero,numeroDecimalTransformado)

    return HttpResponse(documento)


"""hacer un form que le pegue al endpoint y lo redirija"""


def paginaDeJUegos(request):
    return render(request,"paginaJuego.html")


def paginaDeJUegos2(request):
    return render(request,"paginaJuego2.html")

def muni(request):
    return render(request,"proyectoMuni.html")