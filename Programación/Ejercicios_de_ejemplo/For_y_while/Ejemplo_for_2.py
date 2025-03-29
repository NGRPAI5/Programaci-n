#For contador in range (0, 10):
    
var=0
total=0 
maximo=int(input("Introduce un máximo: "))
minimo=int(input("Introduce un mínimo: "))

for contador in range(minimo,maximo):
    total=total+contador
#Para que diga el resultado final y no la lista entera de números.
print(total)

