from django.db import models
from backend.models import CreatedUpdatedModel, SoftDeletedModel

class Profesor(SoftDeletedModel, CreatedUpdatedModel):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=150)


	class Meta:
		verbose_name = "Profesor"
		verbose_name_plural = "Profesores"

	def __str__(self):
		return self.nombre +" "+ self.apellido
	