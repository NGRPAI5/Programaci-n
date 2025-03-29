#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no.
      
lista=["casa", "mesa", "sal", "sol", "agua", ""]
lista_2=["casa", "luz", "tres", "sol", "tren", "pan"]
lista_repetida=[]
lista_no_repetida=[]

for valor_a, valor_b in zip(lista, lista_2):
    if valor_b==valor_a:
        lista_repetida.append(valor_b)
        
    else:
        lista_no_repetida.append(valor_b)
        
print("Están repetidas:", lista_repetida)
print("No están repetidas:", lista_no_repetida)
        