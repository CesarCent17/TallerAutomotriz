class Comprobar:

    def comprobar(self, cedula, lista):
        obj = None
        for i in range(len(lista)):
            if cedula == lista[i].cedula:
                obj = lista[i]
                break
        return obj

    def indice(self, cedula, lista):
        indice = None
        for i in range(len(lista)):
            if cedula == lista[i].cedula:
                indice = i
                break
        return indice

    def clave(self, cuenta):
        ok = True
        while ok == True:
                contraseña = input("Contraseña: ")
                if contraseña == cuenta.contraseña:
                    #contraseña == cuenta.contraseña
                    ok = False
                elif contraseña != cuenta.contraseña:
                    print("Error, intentelo nuevamente\n")
        return contraseña

    def indicexd(self, cedula, lista):
        numeroderegistros = lista.count(cedula)




        listaindices = []
        for i in range(numeroderegistros):
            for i in range(len(lista)):
                if cedula == lista[i].cedula:
                    indice = i
                    listaindices.append(indice)
                break
        print(listaindices)
        #return listaindices






