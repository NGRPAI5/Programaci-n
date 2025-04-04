#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

var_1=str(input("Inserta una frase: "))
palabra_1=var_1.find("madruga")
palabra_2=var_1.find("Dios")
palabra_3=var_1.find("dios")

if "madruga" in var_1:
    print(f"La palabra madruga está en la frase y en el índice {palabra_1}")
    
if "Dios" in var_1:
    print(f"La palabra Dios está en la frase y en el índice {palabra_2}")
    
if "dios" in var_1:
    print(f"La palabra dios está en la frase y en el índice {palabra_3}")
    
else:
    print("La palabra no está en la frase")
