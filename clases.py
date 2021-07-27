#  archivo de clases y funciones

#  ********************* Imports ********************

import sys
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown
from datos import *
import csv 
import os

#  ******************** Variabls globales **********
guardar={}


#  ********************* funciones ******************


def borrarPantalla():  # Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


console = Console()


def listadoTipos():
    console.print(Markdown("# Opciones de Revoques"))
    table = Table(show_header=True, header_style="bold steel_blue1")
    table.add_column("Índice", style="dim", width=30, justify="center")
    table.add_column("Albañilería", style="dim", width=120, justify="left")
    i = 0
    for i in range(0, len(menu)):
        elementos = menu[i]
        indice = elementos["indice"]
        tipo = elementos["tipo"]
        table.add_row(f"{indice}", f"{tipo}")
    console.print(table)


def salir(dato):  # reveer segun funcion Curses
    if dato == 0:
        borrarPantalla()
        print("\n\n\n\n\n\ngracias por usar constapp")
        print("https://github.com/JulioAlaniz")
        print(
            "Para colaborar con el desarrollo de esta aplicación, ingresá al enlace siguiente."
        )
        print("https://cafecito.app/julio-58")
        print("gracias!")
        print("\n\n\n\n\n")
        sys.exit()


#  **************************** Clases *************************


class Materiales:
    def __init__(self, tipo):
        i = 0
        m2 = int(input("Ingrese la cantidad en m2\n"))
        print("")
        for i in range(0, len(tipo)):
            elementos = tipo[i]
            material = elementos["material"]
            cantidad = elementos["cantidad"]
            #print(f"{material}", f"{float(cantidad)*float(m2)}")
            guardar[material]= float(cantidad)*float(m2)
        print('')


class Concreto(Materiales):
    tipo = concreto
    

class ConcretoHidro(Materiales):
    tipo = concretoHidro


class Azotado(Materiales):
    tipo = azotado


class RevGrueso(Materiales):
    tipo = revGrueso


class RevFino(Materiales):
    tipo = revFino


class ColcBaldosas(Materiales):
    tipo = colocBaldosas


class LadComun15(Materiales):
    tipo = ladComun15
 

class LadComun30(Materiales):
    tipo = ladComun30


class LadCeram18x39(Materiales):
    tipo = ladCeram18x39


class HormigonPiedra(Materiales):
    tipo = hormigonPiedra


class HormigonCascotes(Materiales):
    tipo = hormigonCascotes


class Contrapiso10(Materiales):
    tipo = contrapiso10


class CarpetaClavar(Materiales):
    tipo = carpetaClavar


class Menu:
    def __menu__(self):
#        i = 0
#        while i == 0:
            try:
                opcion = int(input("ingrese opcion (de 0 a 13)\n"))
                print("")
                if opcion == 1:
                    carpeta = Concreto(concreto)
                elif opcion == 2:
                    carpetaHidro= ConcretoHidro(concretoHidro)
                elif opcion == 3:
                    azotHidro = Azotado(azotado)
                elif opcion == 4:
                    grueso = RevGrueso(revGrueso)
                elif opcion == 5:
                    fino = RevFino(revFino)
                elif opcion == 6:
                    baldosas = ColcBaldosas(colocBaldosas)
                elif opcion == 7:
                    comun15 = LadComun15(ladComun15)
                elif opcion == 8:
                    comun30 = LadComun30(ladComun30)
                elif opcion == 9:
                    ceramico39 = LadCeram18x39(ladCeram18x39) 
                elif opcion == 10:
                    hpiedra = HormigonPiedra(hormigonPiedra)
                elif opcion == 11:
                    hcascotes = HormigonCascotes(hormigonCascotes)
                elif opcion == 12:
                    contrap10 = Contrapiso10(contrapiso10)
                elif opcion == 13:
                    carpClavar = CarpetaClavar(carpetaClavar)
                elif 0 <= opcion < 14:
                    return opcion
                else:
                    input("la opcion elegida está fuera de rango, vuelva a intentarlo")
            except:
                input("ups! entrada inválida , precione Enter para continuar")
#            else:
#                input("presione Enter para continuar")
#                input("")

class PlanillaClaculo:
    def __init__(self):
        print(guardar)
        archivo = open('../salida.csv', 'a')
#        guardar.write
        archivo.close()
        for k, v in guardar.items():
            print("Cantidad de {0} = {1} kg".format(k,v))
        print('')

        #archivo=open('../salida.txt', 'a')
        #for k, v in guardar.items():
           #archivo.writelines("{0} , {1}\n".format(k,v))
        #archivo.write('\n')
        #archivo.close()
        #print('')

        guardar.clear()



'''
https://code.tutsplus.com/es/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907

DicReader
import csv
with open('name.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
         print(row['first_name'], row['last_name'])

Dicwriter
import csv
with open('name.csv') as csvfile:
reader = csv.DictWriter(csvfile)
for row in reader:
         print(row['first_name'], row['last_name'])
Esta clase es similar a la clase DictWriter y hace lo contrario, que es escribir datos a un archivo CSV. La clase es definida como   csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)

El parámetro fieldnames define la secuencia de llaves que identifican el orden en el cuál los valores en el diccionario son escritos al archivo CSV. A diferencia de DictReader, esta llave no es opcional y debe ser definida para evitar errores cuando se escribe a un CSV.

'''
