"""
Ejercicio 1: Calculadora de factorial

Escribe un programa que solicite al usuario un número entero no negativo y calcule su factorial. El factorial de un número entero positivo 'n' se define como el producto de todos los enteros desde 1 hasta 'n'. Utiliza un bucle para realizar el cálculo y muestra el resultado. Si el usuario ingresa un número negativo, muestra un mensaje de error y pide un número válido.
"""
while True:
    try:
        vPositiveNum = int(input("Por favor ingresa un número Entero Positivo: "))
        if vPositiveNum > 0:
            break
        else:
            print("El número ingresado no es un Número Entero Positivo, intenta de nuevo")
    except ValueError:
        print("El Número ingresado NO es un número Entero")

vResultado = 1    
for i in range(1,vPositveNum+1):
    vResultado = vResultado * i
    
print(f"El Factorial de {vPositveNum} es: {vResultado}")


