#Ejercicio 2

lista=[]
lista_2=[]
lista_3=[]

preguntar=str(input("Introduce una lista de palabras: "))
palabra=str(input("Introduce una lista de palabras: "))
aparecer=0

lista=preguntar
lista.split(preguntar)

aparecer=preguntar.count(palabra)

lista_3=",".join(lista)



print(lista)
print(aparecer)
print(lista_3)