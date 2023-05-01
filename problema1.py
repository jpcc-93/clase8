def sumar_5_enteros():
    #definicion de variables
    lista = []
    contadorwhile = 0
    tamano = 5
    suma = 0

    #ingresamos los numeros:
    while contadorwhile < tamano:
        lista.append(int(input("Ingrese numero " + str(contadorwhile + 1) + ": ")))
        contadorwhile += 1

    #sumamos los numeros:
    contadorwhile = 0
    while contadorwhile < tamano:
        suma += lista[contadorwhile]
        contadorwhile += 1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero,end=', ' )

    print("\nLa suma de todos sus elementos es:")
    print(suma)
