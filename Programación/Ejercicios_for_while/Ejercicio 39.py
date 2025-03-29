#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.

numeros_totales=int(input("Introduce la cantidad de números que deseas introducir: "))
numero_positivo=0
numero_negativo=0
cero=0

for i in range(numeros_totales):
    numero=int(input("Introduce un número: "))
    
    if numero > 0:
        numero_positivo+=1
        
    elif numero < 0:
        numero_negativo+=1
        
    else:
        cero+=1
        
print("La cantidad de números positivos es:", numero_positivo)
print("La cantidad de números negativos es:", numero_negativo)
print("La cantidad de ceros es:", cero)