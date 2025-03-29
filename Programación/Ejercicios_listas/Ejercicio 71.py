#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.

lista=[]

respuesta=input("Quieres empezar s/n: ")

while respuesta=="s":
    letra=input("Introduce una letra: ")
    lista.append(letra)
    lista2=set(lista)
    respuesta=input("Deseas repetir s/n: ")
    
print(lista2)