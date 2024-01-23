"""
Ejercicio 2: Contador de números pares e impares

Escribe un programa que solicite al usuario un número entero positivo. Luego, utiliza un bucle para contar y mostrar la cantidad de números pares e impares en el rango desde 1 hasta el número ingresado por el usuario. Finalmente, muestra los resultados.

Por ejemplo, si el usuario ingresa el número 10, el programa debe mostrar algo como:

mathematica
Copy code
Números pares: 5
Números impares: 5
Este ejercicio te permitirá practicar el uso de bucles, condicionales y contar elementos en un rango.

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

vTotalPar = 0
vTotalImpar = 0
for i in range(1,vPositiveNum+1):
    varPI = i % 2
    if varPI == 0:
        #Es Par
        vTotalPar+= 1
    else:
        #Es Impar
        vTotalImpar+= 1

print(f"El Número Total de Números Pares es: {vTotalPar}")
print(f"El Número Total de Números Impares es: {vTotalImpar}")