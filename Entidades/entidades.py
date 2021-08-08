

#CLASES PERSONAS
class vendedor:
    def __init__(self, nombre, apellido, cedula, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.contraseña = contraseña

class cliente(): #heredar vendedor
    def __init__(self, nombre, apellido, cedula, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        # super().__init__(nombre, apellido, cedula)

#CLASES AUTO
class Automotriz:
    def __init__(self, cedula, modelo, year, matricula):
        self.cedula = cedula
        self.modelo = modelo
        self.year = year
        self.matricula = matricula




