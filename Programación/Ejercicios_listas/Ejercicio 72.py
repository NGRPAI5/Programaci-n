#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista.

vocal_a=["a", "á", "à"]
vocal_e=["e", "é", "è"]
vocal_i=["i", "í", "ì"]
vocal_o=["o", "ó", "ò"]
vocal_u=["u", "ú", "ù"]
lista=[]

respuesta=input("Deseas empezar s/n: ")

while respuesta=="s":
    letra=input("Introduce una letra: ")
    
    if letra in vocal_a:
        letra="a"
        
    if letra in vocal_e:
        letra="e"
        
    if letra in vocal_i:
        letra="i"
        
    if letra in vocal_o:
        letra="o"
        
    if letra in vocal_u:
        letra="u"
    
    if letra not in lista:
        lista.append(letra)
        
    respuesta=input("Quieres continuar s/n: ")

print(lista)
