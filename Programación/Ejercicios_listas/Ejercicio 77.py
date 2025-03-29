#77. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo. 


lista=["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]
lista_2=[elemento.lower() for elemento in lista]
lista_numeros=[]
lista_letras=[]

direccion=str(input("Deseas ver los números y las letras en orden ascendente o descendente A/D: "))

for i in lista_2:
    
    if i.isnumeric():
        lista_numeros.append(i)
        
    else:
        lista_letras.append(i)

if direccion == "a" or direccion == "A":
    lista_numeros.sort()
    lista_letras.sort()           
    print(lista_numeros)
    print(lista_letras)
    
else:
    lista_numeros.sort(reverse=True)
    lista_letras.sort(reverse=True)           
    print(lista_numeros)
    print(lista_letras)
