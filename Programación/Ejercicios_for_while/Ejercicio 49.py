#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

palabra_secreta=str(input("Introduce una palabra secreta: "))

for i in palabra_secreta:
    letra=str(input("Introduce una letra: "))
    if letra in palabra_secreta:
        posicion=(palabra_secreta.find(letra))+1
        for j in range(len(palabra_secreta)):
            if palabra_secreta[j]==letra:
                posicion_2=j+1
            
            else:
                posicion_2=0
         
        if posicion_2>0:
            print("La letra se encuentra en la posición", posicion)
            print("La letra se encuentra en la posición", posicion_2)
            
        else:
            print("La letra se encuentra en la posición", posicion)

    else:
        print("La letra no existe")