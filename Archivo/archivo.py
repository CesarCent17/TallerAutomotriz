from Entidades.entidades import *

class bloc_arch:

    def crearAr(self, nombre, cadena, modo):
        archivo = open(nombre, modo)
        archivo.write(cadena)
        archivo.close()

    def getDatos_admin(self, nombre):
        listaadmins = []
        archivo = open(nombre, "r")
        for linea in archivo.readlines():
            tupla = linea.split(";")

            obAdmin = vendedor(tupla[0], tupla[1], tupla[2], tupla[3])
            listaadmins.append(obAdmin)
        return listaadmins

    def getDatos_cliente(self, nombre):
        listaclientes = []
        archivo = open(nombre, "r")
        for linea in archivo.readlines():
            tupla = linea.split(";")

            obClient = cliente(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
            listaclientes.append(obClient)
        return listaclientes

    def getDatos_au(self, nombre):
        listaau = []
        archivo = open(nombre, "r")
        for linea in archivo.readlines():
            tupla = linea.split(";")

            obau= Automotriz(tupla[0], tupla[1], tupla[2], tupla[3])
            listaau.append(obau)
        return listaau






