#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

var_1=str(input("Introduce una letra por teclado: "))

if var_1.islower()==True:
    print(f"Está en minúsculas la {var_1}")

elif var_1.isupper()==True:
    print(f"Está en mayúsculas la {var_1}")
    
elif var_1.isnumeric()==True:
    print(f"Lo que has introducido es un número, es el número {var_1}")
    
else:
    print(f"El valor introducido por teclado es un símbolo, es el símbolo {var_1} ")
    
    