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



class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	producido = models.DateTimeField(auto_now_add=True, blank=True)
	costo = models.DecimalField(max_digits=5, decimal_places=2)
	precio = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"
		ordering = ["nombre"]

	def __str__(self):
		return self.nombre

class ProductoInventario(Producto):

	class Meta:
		verbose_name = "ProductoInventario"
		verbose_name_plural = "ProductoInventarios"
		ordering = ["producido"]
		proxy = True

	def __str__(self):
		return "Producido: " + str(self.producido)
	
class ProductoVenta(Producto):

	class Meta:
		verbose_name = "ProductoVenta"
		verbose_name_plural = "ProductoVentas"
		ordering = ["precio"]
		proxy = True

	def __str__(self):
		return "Precio de venta: Q." + str(self.precio)
	