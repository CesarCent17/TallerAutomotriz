from Inputs.inputs import *

class men:
    def __init__(self):
        self.ObE = Limitador()

    def MeUs(self, lista):
        for i in range(len(lista)):
            print(str(i+1)+".- "+lista[i])

        op = -1
        while op < 1 or op > len(lista):
            op = self.ObE.Int("\nIngrese una opcion: ")

        return op



