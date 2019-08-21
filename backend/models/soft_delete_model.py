from django.db import models
from django.db.models import QuerySet



class SoftDeleteQuerySet(QuerySet):

	def delete(self):
		"""Cuando se eliminan varios registros a la vez. Por ejemplo en talbas maestro-esclavo"""
		query = super(SoftDeleteQuerySet, self)
		count = 0 #Devolver el número de registros afectados
		count = query.update(estado=False)
		return count


class SoftDeleteManager(models.Manager):
	def __init__(self, *args, **kwargs):
		super(SoftDeleteManager, self).__init__(*args, **kwargs)

	def get_queryset(self):
		return SoftDeleteQuerySet(self.model).filter(estado=True)


class SoftDeletedModel(models.Model):
	"""Sobrescribe el método delete de la clase Model para ejecutar un soft delete 	"""
	estado = models.BooleanField(default=True)
	#Se sobrescribe el Manager por defecto de models para añadir el método soft_delete a queryset
	objects = SoftDeleteManager() 
	original_objects = models.Manager()

	class Meta:
		abstract = True

	def delete(self):
		self.estado = False
		self.save()
