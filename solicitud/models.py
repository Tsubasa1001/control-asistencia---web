from django.db import models
from django.utils import timezone
from empleado.models import Empleado
from cliente.models import Cliente
from material.models import Material
# Create your models here.

class EstadoSolicitud(models.Model):
	nombre = models.CharField(max_length=200)
	detalle = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class TipoSolicitud(models.Model):
	nombre = models.CharField(max_length=200)
	detalle = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Solicitud(models.Model):
	idm = models.IntegerField(null=False) 
	hora = 	models.DateTimeField(default=timezone.now)
	detalle = models.CharField(max_length=200)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	tipo = models.ForeignKey(TipoSolicitud, on_delete=models.CASCADE)
	estado = models.ForeignKey(EstadoSolicitud, on_delete=models.CASCADE, null=True)#poner valor por defecto de estado

	def __str__(self):
		return u'%s' %(self.cliente) 

class Asignacion(models.Model):
	hora_inicio = models.DateTimeField(default=timezone.now, null=True)##	
	hora_fin = models.DateTimeField(default=timezone.now, null=True)####
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
	material = models.ForeignKey(Material, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.solicitud)




#reporte de lista de solicitud por clientexempleadoxmateriales
#reporte de solicitud
