from Entidades.entidades import *
from Inputs.inputs import *
from Menu.generarmenu import *
from Check.Comprobacion import *
from Archivo.archivo import *

class Core:
    def __init__(self):
        self.ob_entrada = Limitador() #CEDULA 10 DIGITOS - INGRESAR ENTERO
        self.ob_menu = men() #IMPRIME MENU
        self.ob_check = Comprobar() #COMPRUEBA LA CEDULA, DEVUELVE OBJ
        self.ob_archi = bloc_arch() #OBJETO TIPO ARCHIVO

    def main(self):
        print("\t\t Taller Automotriz")
        tupla = ("Crear Cuenta", "Iniciar Sesion", "Salir")
        opcion = self.ob_menu.MeUs(tupla)
        if opcion == 1:
            self.crear_cuenta_admin()
            self.main()

        elif opcion == 2:
            #print("Se encuentra en desarrollo")
            self.iniciar_sesion()

        elif opcion == 3:
            print("Adios")

    #Crear cuenta admin
    def crear_cuenta_admin(self):
        print("\n")
        print("\t\t Crear cuenta")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = self.ob_entrada.ced("Cedula: ")
        contraseña = input("Contraseña: ")
        lista_user = self.ob_archi.getDatos_admin("Admin.txt")
        cuenta = self.ob_check.comprobar(cedula, lista_user)
        if cuenta != None:
            print("Cuenta ya existe\n")
        elif cuenta == None:
            admin = vendedor(nombre, apellido, cedula, contraseña)
            lista_user.append(admin)
            msg = admin.nombre+";"+admin.apellido+";"+admin.cedula+";"+admin.contraseña+";\n"
            self.ob_archi.crearAr("Admin.txt", msg, "a")
            print("Cuenta creada!\n")

    def iniciar_sesion(self):
        print("\n")
        lista_user = self.ob_archi.getDatos_admin("Admin.txt")
        cedula = self.ob_entrada.ced("Cedula: ")
        cuenta = self.ob_check.comprobar(cedula, lista_user)

        if cuenta != None: #Cuenta existe
            contraseña = self.ob_check.clave(cuenta)
            print("Iniciando sesion...")
            self.menucuenta(cuenta)

        elif cuenta == None: #Cuenta no existe
            print("Usted no tiene cuenta\n")
            self.main()

    #menu de inicio de sesion
    def menucuenta(self, cuenta):
        print("\nBienvenido!")
        tupla = ("Crear cuenta de cliente", "Crear registro automovilistico", "Administrar clientes", "Configuracion", "Atras")
        opcion = self.ob_menu.MeUs(tupla)

        if opcion == 1:
            self.crearcuenta_cliente()
            self.menucuenta(cuenta)

        elif opcion == 2:
            self.crear_registro_au()
            self.menucuenta(cuenta)

        elif opcion == 3:
            self.administrar_clientes(cuenta)

        elif opcion == 4:
            print("\n")
            self.configuracion_admin(cuenta)


        elif opcion == 5:
            print("\n")
            self.main()

    #Opcion 1
    def crearcuenta_cliente(self):
        print("\n")
        print("\t\t Crear cuenta de cliente")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = self.ob_entrada.ced("Cedula: ")
        direccion = input("Direccion: ")
        telefono = input("Telefono: ")
        lista_cliente = self.ob_archi.getDatos_cliente("Cliente.txt")
        cuenta = self.ob_check.comprobar(cedula, lista_cliente)
        if cuenta != None:
            print("Cuenta ya existe\n")
        elif cuenta == None:
            objCliente = cliente(nombre, apellido, cedula, direccion, telefono)
            lista_cliente.append(objCliente)
            msg = objCliente.nombre + ";" + objCliente.apellido + ";" + objCliente.cedula + ";" + objCliente.direccion + ";"\
            + objCliente.telefono + ";\n"
            self.ob_archi.crearAr("Cliente.txt", msg, "a")
            print("Cuenta creada!\n")

    #Opcion 2
    def crear_registro_au(self):
        print("\n")
        print("\t\t Crear registro automovilistico")
        cedula = self.ob_entrada.ced("Ingrese la cedula del cliente: ")
        lista_cliente = self.ob_archi.getDatos_cliente("Cliente.txt")
        cuenta = self.ob_check.comprobar(cedula, lista_cliente)
        if cuenta == None:
            print("Error, para crear un registro el cliente debe tener cuenta\n")

        elif cuenta != None:
            modelo = input("Modelo: ")
            year = self.ob_entrada.Int("Año: ")
            matricula = input("Matricula: ")
            lista_au = self.ob_archi.getDatos_au("Automovilistico.txt")
            objAu = Automotriz(cedula, modelo, year, matricula)
            lista_au.append(objAu)
            msg = objAu.cedula + ";" + objAu.modelo + ";" + str(objAu.year) + ";" + objAu.matricula + ";\n"
            self.ob_archi.crearAr("Automovilistico.txt", msg, "a")
            print("Registro ingresado con exito\n")

    #Opcion 3
    #Administrar cuentas de clientes
    def administrar_clientes(self, cuenta):
        print("\n")
        print("\t\t Administrar clientes")
        tupla = ("Listar", "Listar registros de clientes", "Editar", "Eliminar", "Atras")
        opcion = self.ob_menu.MeUs(tupla)

        if opcion == 1:
            self.listarclientes()
            self.administrar_clientes(cuenta)

        elif opcion == 2:
            self.listarregistrosau()
            self.administrar_clientes(cuenta)

        elif opcion == 3:
            self.editarcliente()
            self.administrar_clientes(cuenta)

        elif opcion == 4:
            self.eliminarcliente(cuenta)

        elif opcion == 5:
            self.menucuenta(cuenta)

    def listarclientes(self):
        print("\n")
        print("\t\t Lista de clientes")
        print("\n")
        lista_cliente = self.ob_archi.getDatos_cliente("Cliente.txt")
        listanombres = []
        listaapellidos =  []
        listacedulas = []
        for i in range(len(lista_cliente)):
            listanombres.append(lista_cliente[i].nombre)
            listaapellidos.append(lista_cliente[i].apellido)
            listacedulas.append(lista_cliente[i].cedula)
        for i in range(len(listanombres)):
            print(f"Cliente: {listanombres[i]} {listaapellidos[i]}\n"
                  f"Cedula: {listacedulas[i]}\n")

    def listarregistrosau(self):
        print("\n")
        print("\t\t Lista de registros de clientes")
        print("\n")
        listacedulas = []
        listamodelos = []
        listayear = []
        listamatriculas = []
        lista_cliente = self.ob_archi.getDatos_cliente("Cliente.txt")
        lista_au = self.ob_archi.getDatos_au("Automovilistico.txt")

        for i in range(len(lista_au)):
            listacedulas.append(lista_au[i].cedula)
            listamodelos.append(lista_au[i].modelo)
            listayear.append(lista_au[i].year)
            listamatriculas.append(lista_au[i].matricula)

        for i in range(len(listacedulas)):
            print(f"Cliente con la cedula: {listacedulas[i]}\n"
                    f"Modelo: {listamodelos[i]}\n"
                    f"Año: {listayear[i]}\n"
                    f"Matricula: {listamatriculas[i]}\n")

    def editarcliente(self):
        print("\n")
        print("\t\t Editar cliente")
        cedula = self.ob_entrada.ced("Ingrese la cedula del cliente: ")
        lista_cliente = self.ob_archi.getDatos_cliente("Cliente.txt")
        objCliente = self.ob_check.comprobar(cedula, lista_cliente)
        if objCliente == None:
            print("Error, esta cuenta no existe\n")

        elif objCliente != None:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            cedula = self.ob_entrada.ced("Cedula: ")
            direccion = input("Direccion: ")
            telefono = input("Telefono: ")
            objCliente.nombre = nombre
            objCliente.apellido = apellido
            objCliente.cedula = cedula
            objCliente.direccion = direccion
            objCliente.telefono = telefono
            msg = ""
            for i in range(len(lista_cliente)):
                msg = msg + lista_cliente[i].nombre +";"+ lista_cliente[i].apellido +";"+ lista_cliente[i].cedula+";"\
                    +lista_cliente[i].direccion +";"+ lista_cliente[i].telefono +";\n"

            self.ob_archi.crearAr("Cliente.txt", msg, "w")
            print("Datos actualizados!")

    def eliminarcliente(self, cuenta):
        print("\n")
        print("\t\t Eliminar cliente")
        print("Nota: al momento de eliminar la cuenta del cliente se eliminaran sus registros")
        cedula = self.ob_entrada.ced("Ingrese la cedula del cliente: ")
        lista_cliente = self.ob_archi.getDatos_cliente("Cliente.txt")
        indice = self.ob_check.indice(cedula, lista_cliente)
        if indice == None:
            print("Error, esta cuenta no existe")
            self.administrar_clientes(cuenta)
        elif indice != None:
            respuesta = input("¿Estas seguro S/N?: ")
            if respuesta == "n" or respuesta == "N":
                self.administrar_clientes(cuenta)

            elif respuesta == "s" or respuesta == "S":
                lista_cliente.pop(indice)
                msg = ""
                for i in range(len(lista_cliente)):
                    msg = msg + lista_cliente[i].nombre + ";" + lista_cliente[i].apellido + ";" + lista_cliente[
                        i].cedula + ";" \
                          + lista_cliente[i].direccion + ";" + lista_cliente[i].telefono + ";\n"

                self.eliminarregistroau(cedula)
                self.ob_archi.crearAr("Cliente.txt", msg, "w")
                print("Cuenta eliminada!")
                self.administrar_clientes(cuenta)

            else:
                print("Ingreso un caracter incorrecto")
                self.administrar_clientes(cuenta)

    def eliminarregistroau(self, cedula):
        lista_au = self.ob_archi.getDatos_au("Automovilistico.txt")
        listadecedulasau = []
        for i in range(len(lista_au)):
            listadecedulasau.append(lista_au[i].cedula)
        numeroderegistros = listadecedulasau.count(cedula)

        if numeroderegistros == 0:
            print("Esta cuenta no tenia registros")#HASTA ACA OK

        elif numeroderegistros != 0:

            for i in range(numeroderegistros):
                lista_au = self.ob_archi.getDatos_au("Automovilistico.txt")
                indice = self.ob_check.indice(cedula, lista_au)
                lista_au.pop(indice)
                msg = ""

                for i in range(len(lista_au)):
                    msg = msg + lista_au[i].cedula + ";" + lista_au[i].modelo + ";" + str(lista_au[i].year)+ ";" \
                    + lista_au[i].matricula + ";\n"
                self.ob_archi.crearAr("Automovilistico.txt", msg, "w")
            print("Los registros automovilisticos del cliente han sido eliminados correctamente")








        #indice = self.ob_check.indicexd(cedula, lista_au)
        """for i in range(len(lista_au)):
            numeroderegistros = lista_au[i].cedula #encontrar las veces que se repite la cedula
        print(numeroderegistros)"""

    #Opcion 4
    #Configuracion de cuenta del administrador
    def configuracion_admin(self, cuenta):
        print("\t\t Configuracion del administrador")
        tupla = ("Editar", "Atras")
        opcion = self.ob_menu.MeUs(tupla)

        if opcion == 1:
            self.editar_admin()
            self.main()

        elif opcion == 2:
            self.menucuenta(cuenta)

    def editar_admin(self):
        print("\n")
        print("\t\t Editar cuenta del administrador")
        lista_user = self.ob_archi.getDatos_admin("Admin.txt")
        cedula = self.ob_entrada.ced("Cedula actual: ")
        cuenta = self.ob_check.comprobar(cedula, lista_user)
        print("\n")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = self.ob_entrada.ced("Cedula: ")
        contraseña = input("Contraseña: ")
        cuenta.nombre = nombre
        cuenta.apellido = apellido
        cuenta.cedula = cedula
        cuenta.contraseña = contraseña
        msg = ""
        for i in range(len(lista_user)):
            msg = msg+lista_user[i].nombre+";"+lista_user[i].apellido+";"+lista_user[i].cedula+";"+lista_user[i].contraseña+";\n"
        self.ob_archi.crearAr("Admin.txt", msg, "w")
        print("Cuenta editada correctamente!\n")




























