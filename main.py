'''
hasta ahora se a trabajado con variables que
permiten almacenar un unico valor
'''

edad = 12

altura = 1.79

nombre =  "Juan"

estado = True

'''
en python podemos usar 
una variable que almacen una coleccion de datos
y luego accederla por medio se un sub indice
'''

#lista de enteros
lista1 = [10, 5, 3, 9]

#lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4]

#lista de string
lista3 = ["lunes","martes","miercoles"]

#lista de distintos tipos
lista4 = ["juan",45, 1.92,False]



if __name__ == '__main__':

    '''
    cantidad de elementos de cada lista con la palabra len
    '''

    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1 [0] = 1
    print()
    print(lista1[3])