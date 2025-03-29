#Ejercicio_1

lista=[]
lista_2=[]
numeros=str(input("Introduce 6 números separados por guión: "))
lista=numeros
lista.split(numeros)
max_1=lista[0]
min_1=lista[0]
suma=0
media=0
numero=0

for i in lista:
    if i > max_1:
        max_1=i
            
    else:
        min_1=i
        

print(max_1)
print(min_1)
print(round(media,3))
print(lista_2)
