from django.db import models

class CreatedUpdatedModel(models.Model):
	"""Sobrescribe el método delete de la clase Model para ejecutar un soft delete 	"""
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True
	