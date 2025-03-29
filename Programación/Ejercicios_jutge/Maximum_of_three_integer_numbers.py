preguntar=input()

lista=preguntar.split()
numeros=[int(num) for num in lista]

maximo=max(numeros)

print(maximo)