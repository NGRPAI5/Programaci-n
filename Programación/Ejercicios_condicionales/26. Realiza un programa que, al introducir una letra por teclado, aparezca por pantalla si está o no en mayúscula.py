#Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

var_1=str(input("Introduce una letra por teclado: "))
    
if var_1.islower()==True:
    print(f"Está en minúsculas la {var_1}")
    
elif var_1.isupper()==True:
    print(f"Está en mayúsculas la {var_1}")
    
else:
    print(f"¿Es la letra {var_1} una letra?")