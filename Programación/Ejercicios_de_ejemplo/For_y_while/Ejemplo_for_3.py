#For contador in string:
    
var="12345"
#Esta variable se utiliza para contar el número de caracteres del string.
contar=0

for recorrer in var:
    #Sumar 1 a contador.
    contar+=1
    print(recorrer)
print(f"El total de caracteres del string es de: {contar}")