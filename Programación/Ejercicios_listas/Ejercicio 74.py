#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.

lista=["casa", "mesa", "sal", "sol", "agua", ""]
lista_2=["casa", "luz", "tres", "sol", "tren", "pan"]
lista_repetida=[]
lista_no_repetida=[]

for valor_a, valor_b in zip(lista, lista_2):
    if valor_b==valor_a:
        lista_repetida.append(valor_b)
        
    else:
        lista_no_repetida.append(valor_b)
        lista_no_repetida.append(valor_a)
        
print("Están repetidas:", lista_repetida)
print("No están repetidas:", lista_no_repetida)
        