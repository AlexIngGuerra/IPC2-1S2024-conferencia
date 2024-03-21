class Nodo:

    def __init__(self, dato, next = None) -> None:
        self.dato = dato
        self.next = next


class ListaSimple:
    
    def __init__(self) -> None:
        self.inicio = None

    def insertar(self, dato):
        nuevo = Nodo(dato, None)

        if(self.inicio == None):
            self.inicio = nuevo
            return

        aux = self.inicio
        while aux.next != None:
            aux = aux.next
        aux.next = nuevo        

        
    def getDot(self):
        if(self.inicio == None):
            print("Lista Vacia")
            return
        
        idnodo = -1
        cadena = "digraph{\nnode[shape=record];\nrankdir=\"LR\";\n"

        # Graficar Inicio
        idnodo += 1
        dotNode = "{}[label=\"{}\"];\n".format(idnodo, self.inicio.dato)
        cadena = cadena + dotNode

        # Graficar el resto de la lista
        aux = self.inicio.next
        while aux != None:
            idnodo += 1
            dotNode = "{}[label=\"{}\"];\n".format(idnodo, aux.dato)
            dotNext = "{}->{}\n".format(idnodo-1, idnodo)
            cadena = cadena + dotNode + dotNext
            aux = aux.next


        cadena = cadena + "\n}"
        return cadena