#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas.

numero_secreto=False
pares=0
impares=0
positivos=0
negativos=-1
ceros=0
suma_total=+99

while numero_secreto==False:
    numeros=int(input("Introduce números: "))
    
    if numeros>0:
        positivos+=1
        
        if numeros % 2 == 0:
            pares+=1
            
        elif numeros % 2 == 1:
            impares+=1
            
        elif numeros == -99:
            numero_secreto=True
            
        else:
            ceros+=1
            
    else:
        negativos+=1
        
        if numeros == -99:
            numero_secreto=True
            
        elif numeros % 2 == 0:
            pares+=1
            
        elif numeros % 2 == 1:
            impares+=1
            
        else:
            ceros+=1
        
    suma_total+=numeros
    
print("El total de números pares es de:", pares)
print("El total de números impares es de:", impares)
print("El total de números positivos es de:", positivos)
print("El total de números negativos es de:", negativos)
print("El total de ceros es de:", ceros)
print("La suma total de todos los números es de:", suma_total)
