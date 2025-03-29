#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.

import random

tirar=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0

while tirar<100:
    numero=random.randint(1,6)
    tirar+=1
    
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
        
print(f"Los el total de veces que se repite uno es de:", uno)
print(f"Los el total de veces que se repite dos es de:", dos)
print(f"Los el total de veces que se repite tres es de:", tres)
print(f"Los el total de veces que se repite cuatro es de:", cuatro)
print(f"Los el total de veces que se repite cinco es de:", cinco)
print(f"Los el total de veces que se repite seis es de:", seis)
        