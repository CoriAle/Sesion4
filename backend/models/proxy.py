from django.db import models

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
	