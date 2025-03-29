#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while.

import random

numero_secreto=random.randint(1,5)
intentos=3
acabar=False

while acabar==False:
    numero_usuario=int(input("Introduce un número: "))
    intentos-=1
    
    if numero_usuario==numero_secreto:
        print("Ese es el número secreto")
        break
        
    else:
        print("No lo es.")
        
    if intentos==0:
        acabar=True
        
    else:
        acabar=False