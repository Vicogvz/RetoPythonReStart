"""
Descripción: Escribe una función que tome una cadena de caracteres que contiene solo paréntesis ( y ) y determine si la secuencia de paréntesis es válida. Una secuencia de paréntesis es válida si cada paréntesis abierto se cierra con un paréntesis correspondiente en el orden correcto. Por ejemplo, "(())()" y "()" son secuencias válidas, pero ")(" y "(()" no lo son. 
"""
#Inicializar la pila
vPila = []

#Pedir cadena de Paréntesis sin espacios.
#Pude aceptar espacios y hacer un replace, pero mejor desde un inicio valido que se ingrese la cadena sin espacios.
while True:
    vParentesis = input("Por Favor Ingresa una Cadena de Solo Paréntesis y Sin espacios: ")
    #Validar si la cadena contiene solo Paréntesis. La función all se asegura que en toda la cadena vParentesis hayan solo '(' o ')'
    if all(caracter == '(' or caracter == ')' for caracter in vParentesis):
        break
    else:
        print("La entrada No es válida...")

#Si Total caracteres es impar, secuencia correcta no se cumplirá y no se recorre la cadena.
vTotCaracter = vParentesis.__len__()
vResiduo = vTotCaracter % 2

#Si el Total de caracteres es par(vResiduo == 0), convertimos el string en pila y lo recorremos.
#vPila.extend(vParentesis) convierte la variable vPila en Pila/Lista con el contenido de vParentesis
if vResiduo == 0:
    vPila.extend(vParentesis)
    #Siempre inicia en 0
    i=0
    #Recorrer la pila
    while i < len(vPila):
        if i > 0 and vPila[i] == ')' and vPila[i-1] == '(':
            #Se encontró un paréntesis de cierre ')' en i
            vPila.pop(i)  #Eliminar el paréntesis de Cierre
            vPila.pop(i-1) #Eliminar el paréntesis de Apertura '('
            i = i-1 #Regresar el indice al caracter anterior.
        elif vPila[i] == ')':
            #En posición 0 se encontró paréntesis de cierre ')'.
            break
        else:
            i+=1

    if len(vPila) > 0:
        #La pila se elimina por pares de apertura y cierre () y debe quedar vacia. Si No queda vacía es porque habían pares como '((' o '((((', etc.
        print("La secuencia correcta de Paréntesis No se Cumple")
        print(vPila)
    else:
        print("La secuencia correcta de Paréntesis Se Cumplió")
else:
    #Número de Paréntesis impar
    print(f"El total de paréntesis ingresados es impar {vTotCaracter}. La secuencia correcta de los Parentesis No se cumple.")    






