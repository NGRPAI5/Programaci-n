#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente.

import random

lista=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"] 
puntos=[]
respuesta=True
punto=8
puntuacion=0
media=0

valor=random.choice(lista)

while respuesta==True:
    palabra=str(input("Introduce una palabra de entre casa, barco, gato, perro, madera, agua, puente, pantalón: "))
    
    if valor==palabra:
        print("Acertaste")
        puntos.append(punto)
        media+=4
        
        partida=str(input("¿Quieres jugar otra partida s/n?: "))
        punto=8
        
        if partida=="s" or partida=="S":
            respuesta=True
            
        else:
            respuesta=False
        
    else:
        print("Sigue juegando")
        punto-=1

puntuacion=sum(puntos)        
print("La puntuación es de:", puntos)
print"Tu puntución ha sido de:", puntuacion)
print("La media de partidas realizadas es de:", media)

if media < puntuacion:
    print("Tienes buena suerte")
    
else:
    print("Dedicate al parchís")
    