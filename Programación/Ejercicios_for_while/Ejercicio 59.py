#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.

import random

numero_secreto=random.randint(0,1000)
intentos=0
numero_correcto=False

while numero_correcto==False:
    numero_usuario=int(input("Introduce un número: "))
    intentos+=1
    
    if numero_usuario==numero_secreto:
        print("Ese es el número secreto")
        numero_correcto=True
        
    else:
        
        if numero_secreto<numero_usuario:
            print("El número secreto es menor.")
            
        else:
            print("El número secreto es mayor.")
            
print("Has acertado el número, era el:", numero_secreto)
print("Has utilizado un total de:", intentos)