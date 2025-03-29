#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir.

respuesta=True
lista=["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]

while respuesta==True:
    eliminar=input("Introduce que valor deseas eliminar: ")
    
    if eliminar.isnumeric():
        if eliminar in lista:
            lista.remove(eliminar)
            print(lista)
            
        else:
            print("El valor introducido no está en la lista.")
            
    else:
        print("Introduce un valor numérico")
        
    repetir=str(input("Quieres volver a repetir s/n: "))
    
    if repetir=="s" or repetir=="S":
        respuesta=True
        
    else:
        respuesta=False
