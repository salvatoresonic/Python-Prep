import sys
print(sys.path)


class Funciones:
    def __init__(self, lista_datos):
        self.lista = lista_datos

    def verifica_primo(self):
        for i in self.lista:
            if (self.__verifica_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def convertir_temp(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__convertir_temp(
                i, origen, destino), 'grados', destino)

    def factorial(self):
        for i in self.lista:
            print('El factorial de', i, 'es', self.__factorial(i))

    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def num_moda(self, lista2):
        num_modal = 0
        repeticiones = 0
        for num in lista2:
            # para cada elemento de la lista cuenta cuantas veces esta presente en la misma
            num_rep = lista2.count(num)
            # si el conteo "num_rep" > "moda" has que "moda" tome ese valor.
            if num_rep > repeticiones:
                repeticiones = num_rep
                num_modal = num
        return ('la moda es', num_modal, 'con', repeticiones, "repeticiones")

    def __convertir_temp(self, valor, origen, destino):

        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * (9/5) + 32)
            elif (destino == 'kelvin'):
                valor_destino = (valor + 273.15)
            else:
                ('parametro destino incorrecto')

        if (origen == 'farenheit'):
            if (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'celsius'):
                valor_destino = ((valor - 32) * (5/9))
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * (5/9) + 273.15)
            else:
                ('parametro destino incorrecto')

        if (origen == 'kelvin'):
            if (destino == 'kelvin'):
                valor_destino = valor
            elif (destino == 'celsius'):
                valor_destino = (valor - 273)
            elif (destino == 'farenheit'):
                valor_destino = (valor - 273 * (9/5) + 32)
            else:
                ('parametro destino incorrecto')

        return (valor_destino)

    def __factorial(self, numero):
        if (type(numero) != int):
            return 'El numero debe ser un entero'
        if (numero < 0):
            return 'El numero debe ser positivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero
