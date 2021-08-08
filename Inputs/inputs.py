class Limitador:

    def ced(self, msg):
        while True:
            ced = input(msg)
            if len(ced) == 10:
                break
            elif len(ced) != 10:
                print("La cedula no es valida\n")
        return ced

    def Int(self, msg):
        while True:
            try:
                n = int(input(msg))
                break
            except ValueError:
                print("Ingrese un numero entero")

        return n


