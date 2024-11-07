from django.db import models

# las tablas aca son objetos, todo esto es poo


class Vecinos(models.Model):
    nombre=models.CharField(max_length=30)
    calle=models.CharField(max_length=50)
    numero=models.IntegerField()
    problema=models.CharField(max_length=20)
    telefono=models.IntegerField()
    dni=models.IntegerField()


class Pedidos(models.Model):
    nombre=models.CharField(max_length=30)
    detalle=models.CharField(max_length=60)
    fecha=models.DateField()
    hecho=models.BooleanField()


class trabajador(models.Model):
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField()
    dni=models.CharField(max_length=30)
    problema=models.CharField(max_length=20)
    detalle=models.CharField(max_length=60)


#las clases son tablas
#primero inicie una app en la carpeta principal con "python3 manage.py startapp gestionMunicipal"
#despues me meti y checkee si estaba bien con "python3 check gestionMuni"
#despues de hacer mis tablas ejecute python3 manage.py makemigrations que genera esta base de datos
#y ahora para generar el codigo sql hacemos python3 manage.py sqlmigrate gestionMunicipal 001
#por ultimo migramos esto a la base de datos original con python3 manage.py migrate



#para agregar registros python3 manage.py shell y ahi from gestionMunicipal.models import y la clase a llenar registros
# vecin=Vecinos(nombre="maria",calle="rivera",numero=997,problema="ramas",telefono=1127586404,dni=40813445)

