from django.db import models

# Create your models here.

class EstadoEmpleado(models.Model):
	nombre = models.CharField(max_length=200)
	detalle = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Cargo(models.Model):
	nombre = models.CharField(max_length=200)
	detalle = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre


class Punto(models.Model):
	latitud = models.DecimalField(max_digits=15, decimal_places=10)
	longitud = models.DecimalField(max_digits=15, decimal_places=10)

class Area(models.Model):
	punto = models.ManyToManyField(Punto)

 
class Zona(models.Model):
	nombre =  models.CharField(max_length=200) 
	detalle = models.CharField(max_length=200)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre
 
class Empleado(models.Model):
	ci = models.CharField(max_length=200)
	codigo_identificacion = models.IntegerField(default=0) 
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	latitud =  models.DecimalField( max_digits=15, decimal_places=10, null=True)
	longitud = models.DecimalField(max_digits=15, decimal_places=5, null=True)
	domicilio = models.CharField(max_length=300, null=True)
	foto = models.ImageField(null=True)
	huella = models.ImageField( null=True)
	telefono = models.CharField(max_length=20)
	costo = models.DecimalField(max_digits=15, decimal_places=5, null=True)
	estado = models.ForeignKey(EstadoEmpleado, on_delete=models.CASCADE)
	cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
	zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre