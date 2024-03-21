class Tabla:

    def __init__(self) -> None:
        self.tabla = [[0, 2, 0], [0, 2, 1], [0, 0, 1]]

    def getDot(self):

        cadena = "graph{\nnode [shape=none];\n"
        cadena = cadena + "base[label=<\n<table>\n"

        for fila in self.tabla:
            cadena = cadena + "<tr>\n"
            for valor in fila:
                if(valor == 0):
                    cadena = cadena + "<td bgcolor=\"{}\">   </td>\n".format("black")
                elif(valor==2):
                    cadena = cadena + "<td bgcolor=\"{}\">   </td>\n".format("aquamarine")
                else:
                    cadena = cadena + "<td bgcolor=\"{}\">   </td>\n".format("white")
                
            cadena = cadena + "</tr>\n"


        cadena = cadena + "</table>\n>]\n"
        cadena = cadena + "\n}"
        return cadena