partido_rojo=""
dpi=" "
partido_azul=""
eleccion=""
rojo=""
verde=""
azul=""
naranja=""
dpi=(input("Ingrese su dpi"))
if len(dpi)<13:
    print("Ingrese la cantidad de 13 números")
if len(dpi)>13:
    print("no valido")
    
if len(dpi)==13:
        print("valido")
        print("Opciones para presidencia: ")
        print("1. Partido rojo")
        print("2. Partido azul")
        eleccion= input("Seleccione hacia que partido es su voto:")
        if eleccion== "Rojo":
            print("su voto ha sido para el partido rojo")

        if eleccion== "Azul":
            print("su voto a sido para el partido azul")

        alcaldia =""
        confirmacion=""
        resumen=""
        print("")
        alcaldia= input("Opciones a elegir: Partido verde, Partido Naranja, Partido rojo, Partido azul ")

        if alcaldia== "Verde":
            print("su voto ha sido para el partido verde")

        if alcaldia== "Naranja":
            print("su voto a sido para el partido naranja")

        if alcaldia== "Rojo":
            print("su voto a sido para el partido rojo")

        if alcaldia== "Azul":
            print("su voto a sido para el partido azul")

        confirmacion= input("Desea confirmar sus votos?")

        if confirmacion== "Si":
            print("Su voto a sido confirmando")
