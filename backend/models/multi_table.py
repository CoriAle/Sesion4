from django.db import models

#Ejemplos multi-tabla
class Lugar(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=80)

	def __str__(self):
		return self.nombre

class Restaurant(Lugar):
	italiano = models.BooleanField(default=False)
	chino = models.BooleanField(default=False)

class Cancha(Lugar):
	grama = models.BooleanField(default=False)
	ancho = models.DecimalField(max_digits=5, decimal_places=2)
	largo = models.DecimalField(max_digits=5, decimal_places=2)

