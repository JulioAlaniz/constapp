#  archivo de clases y funciones
#  ********************* Imports ********************
import sys
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown
from datos import *
import os


#  ********************* funciones ******************

def borrarPantalla():  # Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
console = Console()

def formatPantalla():
    console.print(Markdown("# Opciones de Revoques"))
    table = Table(show_header=True, header_style="bold steel_blue1")
    table.add_column("indice", style="dim", width=30, justify="center")
    table.add_column("tipo de cable", style="dim", width=120, justify="left")
    i = 0
    for i in range(0, len(menu)):
        elementos = menu[i]
        indice = elementos["indice"]
        tipo = elementos["tipo"]
        table.add_row(f"{indice}", f"{tipo}")
    console.print(table)


def materialConcreto():
    i=0
    print('Concreto')
    m2=int(input('Ingrese la cantidad en m2 de revoque\n'))
    for i in range(0, len(concreto)):
        elementos=concreto[i]
        material = elementos["material"]
        cantidad = elementos["cantidad"]
        print(f"{material}", f"{float(cantidad)*float(m2)}")

    
def materialConcretoHidro():
    i=0
    m2=int(input('Ingrese la cantidad en m2 de revoque\n'))
    for i in range(0, len(concretoHidro)):
        elementos=concretoHidro[i]
        material = elementos["material"]
        cantidad = elementos["cantidad"]
        print(f"{material}", f"{float(cantidad)*float(m2)}")

def materialRevGrueso():
    i=0
    m2=int(input('Ingrese la cantidad en m2 de revoque\n'))
    for i in range(0, len(revGrueso)):
        elementos=revGrueso[i]
        material = elementos["material"]
        cantidad = elementos["cantidad"]
        print(f"{material}", f"{float(cantidad)*float(m2)}")

def materialRevFino():
    i=0
    m2=int(input('Ingrese la cantidad en m2 de revoque\n'))
    for i in range(0, len(revFino)):
        elementos=revFino[i]
        material = elementos["material"]
        cantidad = elementos["cantidad"]
        print(f"{material}", f"{float(cantidad)*float(m2)}")
        cemento=float(cantidad)*float(m2)
        input('los totales han sido cargados en excel, presione enter para continuar')



def salir(dato):        # reveer segun funcion Curses
    if dato == 9:
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

class Menu:
    def __menu__(self):
        i = 0
        while i == 0:
            try:
                opcion = int(input("ingrese opcion (de 1 a 9)\n"))
                if 0 < opcion < 10:
                    return opcion
                else:
                    input("la opcion elegida está fuera de rango, vuelva a intentarlo")
            except:
                input("ups! entrada inválida , precione Enter para continuar")
        else:
            input("presione Enter para continuar")
  

def mortero(opcionMortero):
    if opcionMortero == 1:
        materialConcreto()
    elif opcionMortero == 2:
        materialConcretoHidro()
    elif opcionMortero == 3:
        materialRevGrueso()
    elif opcionMortero == 4:
        materialRevFino()
        
