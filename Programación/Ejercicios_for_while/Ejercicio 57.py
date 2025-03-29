#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5.

import random

numero_secreto=random.randint(1,5)

while numero_secreto:
    numero_usuario=int(input("Introduce un número: "))
    
    if numero_usuario==numero_secreto:
        print("Ese es el número secreto")
        break
        
    else:
        print("No lo es.")