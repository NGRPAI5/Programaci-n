#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.

mi_lista=[]
numeros_puestos=0

numeros=int(input("Introduce una cantidad exacta de números que introducirás: "))

while numeros>numeros_puestos:
    introducir=int(input("Introduce un número para almacenar: "))
    mi_lista.append(introducir)
    numeros_puestos+=1
    
    mi_lista.sort()
    
print("La lista ordenada es de:", mi_lista)