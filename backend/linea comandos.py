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

canchas = Cancha.objects.all()
print(canchas.query)
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


gato = Gato.objects.all()
print(gato.query)

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





Profesor.objects.create(
	nombre="Ricardo",
	apellido="Jirafales"
)

Profesor.objects.create(


	nombre="Obi-Wan",
	apellido="Kenobi"
)


Profesor.objects.all()
Profesor.objects.all().delete()
Profesor.original_objects.all()

profe = Profesor.objects.create(
	nombre="Denzel",
	apellido="Crocker"
)

profe.creado


Estudiante.objects.create(
	nombre="Elmo Cifuente",
	telefono="4797789",
	direccion="13 Av. 6-8, zona 3",
	sexo=True,
	carnet="201908078"
)


Docente.objects.create(
	nombre="Noel Gómez",
	telefono="556497",
	direccion="14 Av. 7-2, zona 1",
	titulo="Ing. ",
	nit="1234567k"
)

Docente.objects.all()
Estudiante.objects.all()
Persona.objects.all()