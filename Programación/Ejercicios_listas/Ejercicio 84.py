#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.

import random

#palabra escogida al azar
listaword=""

listadeletras=[]
listadesorden=[]
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]

#escojo al azar una palabra de la LISTA
listaword1=random.choice(lista)

#convierto el valor escogido en un string con las letras separadas
listaword="-".join(listaword1)

#paso las letras a una lista. Cada letra ocupa una posición
listadeletras=listaword.split("-")

repetir=0

while repetir < 3:
    #realizo un bucle para desordenar las letras
    while len(listadeletras)>0:
        letra=random.choice(listadeletras)
        listadesorden.append(letra)
        listadeletras.remove(letra)
    
    palabrasecreta="".join(listadesorden)
    print("FORMA UNA PALABRA CON ", palabrasecreta)
    usuario=input("adivina la palabra: ")
    repetir+=1
    
    while listaword1!=usuario:
        print("error, no has hacertado")
        usuario=input("adivina la palabra: ")
    
    else:
        print("eres un máquina")
    
    print("Forma una palabra con:", palabrasecreta)
    usuario=input("Adivina la palabra: ")
    
    while listaword1!=usuario:
        print("Error, no has acertado")
        usuario=input("Adivina la palabra: ")
        
    else:
        print("Eres una máquina")
        