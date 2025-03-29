import random

numero_secreto=random.randint(1,10)

while numero_secreto:
    numero_usuario=int(input("Introduce un número: "))
    
    if numero_usuario==numero_secreto:
        print("Ese es el número secreto")
        break
        
    else:
        print("No lo es.")