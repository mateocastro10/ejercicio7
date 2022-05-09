class Viajero:
    __dni = 0
    __num_viajero = 0
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, nv, dni, nom, ape, ma):
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__num_viajero = nv
        self.__millas_acum = ma

    def __str__(self):
        s = str(self.__num_viajero) + ' ' + str( self.__nombre) +' ' + str(self.__apellido) + ' ' + str(self.__dni) + ' ' + str(self.__millas_acum) + '\n'
        return s

    def __eq__(self, other):
        b = False
        if self.cantidadTotalMillas() == other:
            b = True
            return b
        elif other == self.cantidadTotalMillas():
            b = True
            return b
        else:
            return b

    def __radd__(self, other):
        self.__millas_acum = other + self.__millas_acum
        return  self.__millas_acum

    def __rsub__(self, other):
        self.__millas_acum = other - self.__millas_acum
        return self.__millas_acum

    def cantidadTotalMillas(self):
        cant1 = self.__millas_acum
        return cant1

    def acumularmillas(self, millas):
        if(type(millas)==int):
            self.__radd__(millas)
            return self.__millas_acum
        else:
            print('TIPO DE DATO INCORRECTO')

    def canjear(self, c):
        if(type(c)==int):
            if c <= self.__millas_acum:
                self.__rsub__(c)
                return self.__millas_acum
            else:
                print("ERROR, MILLAS INSUFICIENTES")
        else:
            print('TIPO DE DATO INCORRECTO')
