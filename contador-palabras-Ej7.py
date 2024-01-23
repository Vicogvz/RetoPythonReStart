"""
Crea un programa que cuente el número de veces que cada palabra aparece en una cadena de texto dada por el usuario. Ignora las diferencias entre mayúsculas y minúsculas y excluye los signos de puntuación.

Consejos: Usa un diccionario para almacenar las palabras y sus conteos. Puedes usar el método split para separar el texto en palabras y el método replace para eliminar la puntuación.
"""
#Importar Función string para usar métodos como str.maketrans para crear Formateadores de cadenas.
import string

def fContar_Palabras(vOracionOrig):
    #Eliminar signos de puntuación de la cadena original: Tercer parametro
    vFormatoS = str.maketrans("", "", string.punctuation)
    vOracionOrig = vOracionOrig.translate(vFormatoS)

    #Convertir a Mayúsculas y dividir en palabras. Split sin parametro divide por espacios
    vLPalabras = vOracionOrig.upper().split()

    #Crear un diccionario para contar las apariciones de cada palabra
    vDContPalabras = {}

    #Contar las palabras en la lista vLPalabras
    for palabra in vLPalabras:
        if palabra in vDContPalabras:
            vDContPalabras[palabra] += 1
        else:
            vDContPalabras[palabra] = 1

    return vDContPalabras


#Solicitar al usuario que ingrese una cadena de texto
vPalabras = input("Por favor Ingrese una oración: ")

#Llamar función fContar_Palabras y Obtener el conteo de palabras en la oración ingresada.
vTotalPalabras = fContar_Palabras(vPalabras)

#Imprimir el resultado
print("\nConteo de palabras:")
for palabra, conteo in vTotalPalabras.items():
    print(f"{palabra}: {conteo}")

