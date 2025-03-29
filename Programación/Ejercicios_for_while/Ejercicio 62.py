#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

numero_uno=int(input("Introduce un primer número: "))
numero_dos=int(input("Introduce un segundo número: "))
pares=""
impares=""

if numero_uno > numero_dos:
    numero_uno, numero_dos = numero_dos, numero_uno

for i in range (numero_uno, numero_dos):
    if numero_uno % 2 == 0:
        pares+=str(numero_uno)
        
        if (numero_dos-2) == numero_uno:
            pares+=""
            
        else:
            pares+="-"
        
    elif numero_uno % 2 == 1:
        impares+=str(numero_uno)
        
        if (numero_dos-1) == numero_uno:
            impares+=""
            
        else:
            impares+="-"
        
    numero_uno+=1
    
print(pares)
print(impares)
    