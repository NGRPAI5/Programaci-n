preguntar=input()

if " " in preguntar:
    lista=preguntar.split()
    numeros=[int(num) for num in lista]
    suma=sum(numeros)
    
else:
    preguntar_2=input()
    lista=preguntar.split()
    lista.append(preguntar_2)
    numeros=[int(num) for num in lista]
    suma=sum(numeros)

print(suma)