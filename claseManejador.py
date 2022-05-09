import csv
from claseViajero import Viajero

class ManejadorViajero:
    def __init__(self):
        self.__listaViajeros = []

    def __str__(self):
        s = ""
        for Viajero in self.__listaViajeros:
            s += str(Viajero) + '\n'
        return s

    def agregarViajero(self, unViajero):
        if(type(unViajero)==Viajero):
            self.__listaViajeros.append(unViajero)
        else:
            print('TIPO DE DATO INCORRECTO')

    def getViajero(self, num):
        if(type(num)==int):
            return self.__listaViajeros[num]
        else:
            print('TIPO DE DATO INCORRECTO')
    def testViajero(self):
        archivo = open('Libro1.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            nv = int(fila[0])
            dni = str(fila[1])
            nom = str(fila[2])
            ape = str(fila[3])
            ma = int(fila[4])
            unViajero = Viajero(nv, dni, nom, ape, ma)
            self.agregarViajero(unViajero)
            print("----------------------------------------------------------")
            print("Cargado con exito")
        archivo.close()
        self.__str__()

    def determina(self):
        otro = int(input('Ingrese valor a comparar: '))
        x = int(input('Ingrese viajero: '))
        if self.__listaViajeros[x-1].__eq__(otro) == True:
            print('las cantidades son iguales')


    def acumula(self):
        c= int(input('ingrese millas'))
        num= int(input('ingrese nro viajero'))
        via=self.getViajero(num-1)
        print(via.acumularmillas(c))

    def canjear(self):
        c= int(input('ingrese millas'))
        num= int(input('ingrese nro viajero'))
        via=self.getViajero(num-1)
        print(via.canjear(c))
