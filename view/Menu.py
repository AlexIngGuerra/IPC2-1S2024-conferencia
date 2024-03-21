from util.estructuras.ListaSimple import ListaSimple
from util.estructuras.Tabla import Tabla
from util.dot.Grafica import generar


def Menu():
    while True:
        print("########### MENU #############")
        print("1. Graficar Lista Simple")
        print("2. Graficar Tabla")
        print("3. Salir")

        opcion = input()
        if(opcion == "1"):
            graficarListaSimple()
        elif(opcion == "2"):
            generarTabla()
        elif(opcion == "3"):
            break


def graficarListaSimple():
    lista = ListaSimple()
    for i in range(0,5):
        lista.insertar(i)
    generar(lista.getDot(), "./graficas/listasimple.svg")

def generarTabla():
    tabla = Tabla()
    generar(tabla.getDot(), "./graficas/tabla.svg")