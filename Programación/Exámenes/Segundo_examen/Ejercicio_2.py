#2

numeros=int(input("Introduce el número de números: "))
numeros_positivos=0
numeros_negativos=0

for i in range(numeros):
    el_numero=int(input("Introduce un número:"))
    if el_numero>0:
        numeros_positivos+=el_numero
        
    else:
        numeros_negativos+=el_numero

        
print("La suma de números positivos es de:", numeros_positivos)
print("La suma de números negativos es de:", numeros_negativos)