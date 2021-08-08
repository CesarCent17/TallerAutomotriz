class gato:
    def __init__(self, nombre):
        self.nombre = nombre
g1 = gato("Kira")
listagatos = []
listagatos.append(g1)
for i in range(len(listagatos)):
    print(listagatos[i].nombre)