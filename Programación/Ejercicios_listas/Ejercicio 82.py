#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra.

import random

lista=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"] 
respuesta=True

valor=random.choice(lista)

while respuesta==True:
    palabra=str(input("Introduce una palabra de entre casa, barco, gato, perro, madera, agua, puente, pantalón: "))
    
    if valor==palabra:
        print("Acertaste")
        respuesta=False
        
    else:
        print("Sigue jugando")
        respuesta=True
