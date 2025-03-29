#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.

palabra=str(input("Introduce una palabra: "))
vocales="aeiouáéíóúAEIOU"
vocales_encontradas=""
consonantes_encontradas=""

for letra in palabra:
    if letra in vocales:
        vocales_encontradas+=letra
            
    else:
        consonantes_encontradas+=letra           
        
print(f"Las vocales de la palabra {palabra} son: {vocales_encontradas}")
print(f"Las vocales de la palabra {palabra} son: {consonantes_encontradas}")
