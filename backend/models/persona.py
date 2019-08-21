from django.db import models

DOCENTE = 1
ESTUDIANTE = 2


class Persona(models.Model):
	ROLES = (
		(DOCENTE, "DOCENTE"),
		(ESTUDIANTE, "ESTUDIANTE"),
	)
	#DATOS DE USUARIOS
	nombre = models.CharField(max_length=150, blank=True)
	rol = models.SmallIntegerField(choices=ROLES, null=True)
	telefono = models.CharField(max_length=10, null=True)
	direccion = models.CharField(max_length=200, blank=True, null=True)
	#DATOS DE DOCENTE
	titulo = models.CharField(max_length=50, blank=True, null=True)
	nit = models.CharField(max_length=50, blank=True, null=True)
	#DATOS ALUMNOS
	sexo = models.NullBooleanField(blank=True, null=True) #True = hombre False = Mujer
	carnet = models.CharField(max_length=20, blank=True,null=True)
	class Meta:
		verbose_name = "Persona"
		verbose_name_plural = "Personas"
	def __str__(self):
		return self.nombre

  


class DocenteManager(models.Manager):
	def get_queryset(self):
		return super(DocenteManager, self).get_queryset().filter(
			rol=DOCENTE)

class EstudianteManager(models.Manager):
	def get_queryset(self):
		return super(EstudianteManager, self).get_queryset().filter(
			rol=ESTUDIANTE)



class Docente(Persona):
	objects = DocenteManager()
	class Meta:
		proxy = True
		ordering = ["nombre"]

	def save(self, *args, **kwargs):
		self.rol = DOCENTE
		super(Docente, self).save(*args, **kwargs)

class Estudiante(Persona):
	objects = EstudianteManager()
	class Meta:
		proxy = True
		ordering = ["carnet"]

	def save(self, *args, **kwargs):
		self.rol = ESTUDIANTE
		super(Estudiante, self).save(*args, **kwargs)