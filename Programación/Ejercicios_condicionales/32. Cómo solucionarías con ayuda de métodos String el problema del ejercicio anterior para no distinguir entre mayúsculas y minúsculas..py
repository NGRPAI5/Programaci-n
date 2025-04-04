#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas.

var_1=str(input("Inserta una frase: "))
todo_minusculas=var_1.lower()
palabra_1=todo_minusculas.find("madruga")
palabra_2=todo_minusculas.find("dios")

if "madruga" in todo_minusculas:
    print(f"La palabra madruga está en la frase y en el índice {palabra_1}")
    
if "dios" in todo_minusculas:
    print(f"La palabra Dios está en la frase y en el índice {palabra_2}")
    
else:
    print("La palabra no está en la frase")
