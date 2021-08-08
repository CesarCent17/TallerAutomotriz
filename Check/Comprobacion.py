class Comprobar:

    def comprobar(self, cedula, lista):
        obj = None
        for i in range(len(lista)):
            if cedula == lista[i].cedula:
                obj = lista[i]
                break
        return obj

    def clave(self, lista, cedula):
        ok = True
        while ok == True:
                contraseña = input("Contraseña: ")
                for i in range(len(lista)):
                    if contraseña != lista[i].contraseña:
                        ok = True
                        print("Error, intentelo nuevamente\n")
                        break
                    elif contraseña == lista[i].contraseña and cedula == lista[i].cedula:
                        contraseña = lista[i].contraseña
                        ok = False
                        break
        return contraseña

    def indice(self, cedula, lista):
        indice = None
        for i in range(len(lista)):
            if cedula == lista[i].cedula:
                indice = i
                break
        return indice




