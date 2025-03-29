#41. Imprime el siguiente patrón utilizando for
texto="54321"

for i in range(0,len(texto)):
    la_longitud=len(texto)
    print(texto)
    texto=texto[1:la_longitud]