from django.db import models
from empleado.models import Zona

class Cliente(models.Model):
	ci = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	latitud =  models.DecimalField(max_digits=15, decimal_places=10, null=True)
	longitud = models.DecimalField(max_digits=15, decimal_places=10, null=True)
	direccion = models.CharField(max_length=200)
	nro_contrato = models.IntegerField(default=0)
	telefono = models.CharField(max_length=20)
	zona = models.ForeignKey(Zona, on_delete=models.CASCADE, null=True)

	def __str__(self):
	    return self.nombre

############# Reporte por cliente ###################
#supongo que sera un metodo....
#####################################################


# Create your models here.
