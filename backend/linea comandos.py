 """
from backend.models import *
lugar = Lugar.objects.create(
	nombre="Parque Central", 
	direccion="Zona 1, Quetzaltenango"
	)
restaurante = Restaurant.objects.create(
	nombre="Lai Lai", 
	direccion="Interplaza", 
	chino=True
	)
cancha = Cancha.objects.create(
	nombre="Futeca", 
	direccion="Zona 3", 
	grama=True, 
	ancho=5.5, largo=10.5)

lugares = Lugar.objects.all()


futeca = lugares[2]
futeca.cancha

lai = lugares[1]
lai.restaurant


	"""

from backend.models import *

Gato.objects.create(
		nombre="pelusa",
		edad=3,
		antirabica= True,
		desparasitante= True

	)

Pez.objects.create(
		nombre="Nemo",
		edad=3,
		color="Dorado",
		tamanio=False
	)


Animal.objects.create(
	nombre="Firulais",
	edad=1,
)


from backend.models import *


Producto.objects.create(
		nombre="Penicilina",
		costo=5.5,
		precio=6.0
	)

ProductoInventario.objects.create(
		nombre="Jarabe para la tos",
		costo=9.86,
		precio=12.0
	)

ProductoVenta.objects.create(
		nombre="Jabón para manos",
		costo=10.80,
		precio=14.50
	)


ProductoVenta.objects.create(
		nombre="Panadol",
		costo=0.80,
		precio=2.00
	)