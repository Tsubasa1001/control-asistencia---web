from django.db import models

# Create your models here.
class Material(models.Model):
	nombre = models.CharField(max_length=200)
	detalle = models.CharField(max_length=200)

	def __str__(self):
			return self.nombre
