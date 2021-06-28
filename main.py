from clases import *

i=0
while i == 0:
	borrarPantalla()
	formatPantalla()
	opcion = Menu()
	opcionMortero = opcion.__menu__()
	print("la opcion elegida es:", opcionMortero, "\n")
	salir(opcionMortero)
	mortero(opcionMortero)
	input('presione una tecla para continuar')
else:
	input('presione una tecla para continuar')