#40. Crea un programa que cuente todos los números pares hasta el número 50.

pares=0
impares=0

for i in range(0,50):
    
    if i % 2 ==0:
        pares+=1
        
    else:
        impares+=1
    
print("El número de pares es:", pares)
print("El número de impares es:", impares)
