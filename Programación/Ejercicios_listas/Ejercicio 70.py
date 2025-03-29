#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.

mi_lista=[]
mi_lista_2=[]
letras_puestas=0

letras=int(input("Introduce la cantidad exacta de palabras que introducirás: "))

while letras>letras_puestas:
    introducir=str(input("Introduce una palabra para almacenar: "))
    mi_lista.append(introducir)
    mi_lista_2.append(introducir)
    letras_puestas+=1
    
    mi_lista.sort()
    mi_lista_2.sort(reverse=True)
    
print("La lista ordenada es de:", mi_lista)
print("La lista ordenada es de:", mi_lista_2)
