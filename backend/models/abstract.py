from django.db import models

class Animal(models.Model):
	"""
	Description: Model Description
	"""
	nombre = models.CharField(max_length=100)
	edad = models.SmallIntegerField()

	class Meta:
		abstract = True

	def __str__(self):
		return "Hola, yo soy: "+self.nombre

class Gato(Animal):
	"""
	Description: Model Description
	"""
	antirabica = models.BooleanField(default=False)
	desparasitante = models.BooleanField(default=False)

class Pez(Animal):
	"""
	Description: Model Description
	"""
	color = models.CharField(max_length=100)
	#tamaño True = Grande, False = Pequeño
	tamanio = models.BooleanField(default=False)