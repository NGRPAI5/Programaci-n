#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).

import math

var_1=float(input("Introduce un número: "))
raiz=math.sqrt(var_1)
resultado_entero=raiz//2

print("El resultado de la raíz cuadrada a partir del número introducidoo es de:",round(raiz,1))
print("El resultado de la división entera a partir de la raíz cuadrada es de:",resultado_entero)
