from util.estructuras.ListaSimple import ListaSimple
from util.dot.Grafica import generar

def Menu():
    while True:
        print("########### MENU #############")
        print("1. Graficar Lista Simple")
        print("2. ")
        print("3. Salir")

        opcion = input()
        if(opcion == "1"):
            graficarListaSimple()
        elif(opcion == "2"):
            print("")
        elif(opcion == "3"):
            break


def graficarListaSimple():
    lista = ListaSimple()
    for i in range(0,5):
        lista.insertar(i)
    generar(lista.getDot(), "./graficas/listasimple.svg")

def generarTabla():
    print("Generando tabla")