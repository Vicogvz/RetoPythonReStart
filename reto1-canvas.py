"""
Write a Python script to: Display all the prime numbers between 1 to 250.
Store the results in a results.txt file.
Test the script. Verify that it produced the expected results in the results.txt file.
"""
#Función que calcula los números primos contenidos en un número dado y regresa valor
def fNumPrimo(vPositiveNum):
    #Variable que guarda los Num Primos
    vNumPrimos = ""
    
    #Calculando los Num Primos
    for i in range(1, vPositiveNum+1):
        vResiduo = i % 2
        if vResiduo == 0 and i != 2:
            #Solo quiero que el flujo continue
            pass
        else:
            #Guardando los Num Primos
            vNumPrimos = vNumPrimos + str(i) + ","
            
    #Eliminamos el ultimo caracter de la cadena ","
    vNumPrimos = vNumPrimos[:-1]
    #Retornando solo los Num Primos
    return vNumPrimos

#Función que guarda una cadena en un archivo .txt, los datos separados por comas
def fGuardarNPArchivo(vDatosArchivo):
    # Ruta del archivo de texto
    file_path = "NumerosPrimos.txt"

    # Abre el archivo en modo escritura ('w' para escribir, 'a' para agregar al final)
    with open(file_path, 'w') as file:
        # Escribe los datos en el archivo, separados por comas
        file.write(vDatosArchivo)

    print(f"Los datos se han guardado en el archivo: {file_path}")

    
print("Programa que despliega los Números Primos del 1 al 250 en un archivo .txt")

#Llamando la función que Calcula los Números Primos contenidos en número dado(250)
vNumPrimosA = fNumPrimo(250)
#Función que guarda strings en un archivo .txt, separados por comas
fGuardarNPArchivo(vNumPrimosA)




