#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos.

import random
import time

inicio = time.time()
duracion=3
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0

while time.time() - inicio < duracion:
    numero=random.randint(1,6)
    
    if numero==1:
        uno+=1
        
    elif numero==2:
        dos+=1
        
    elif numero==3:
        tres+=1
        
    elif numero==4:
        cuatro+=1
        
    elif numero==5:
        cinco+=1
        
    else:
        seis+=1

print(f"El tiempo total ha sido de: {duracion} segundos")
print(f"Los el total de veces que se repite uno es de:", uno)
print(f"Los el total de veces que se repite dos es de:", dos)
print(f"Los el total de veces que se repite tres es de:", tres)
print(f"Los el total de veces que se repite cuatro es de:", cuatro)
print(f"Los el total de veces que se repite cinco es de:", cinco)
print(f"Los el total de veces que se repite seis es de:", seis)
        