"""
Ejercicio 3: Calculadora de Número Primos

Descripción: Escribe una función que tome un número entero y devuelva True si el número es primo y False en caso contrario. Luego, utiliza esta función en un programa que pida al usuario ingresar un número y muestre en pantalla si es primo o no.

Consejos: Recuerda que un número primo es un número mayor que 1 que solo tiene dos divisores: 1 y él mismo.
"""
#print(dir(2.5))

def numPrimo():
    while True:
        try:
            vPositiveNum = int(input("Por favor ingresa un número Entero Positivo: "))
            if vPositiveNum > 0:
                break
            else:
                print("El número ingresado no es un Número Entero Positivo, intenta de nuevo")
        except ValueError:
            print("El Número ingresado NO es un Número Entero")
            
    vResiduo = vPositiveNum % 2
    if vResiduo == 0 and vPositiveNum != 2:
        print(f"El Número ingresado {vPositiveNum} No es un Número Primo")
    else:
        print(f"El Número ingresado {vPositiveNum} Si es un Número Primo")    

#Llamando la función que pide un Número y valida si es Primo o No.
numPrimo()