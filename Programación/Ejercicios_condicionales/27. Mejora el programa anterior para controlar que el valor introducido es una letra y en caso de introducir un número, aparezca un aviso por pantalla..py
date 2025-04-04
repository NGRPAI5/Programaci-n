#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

var_1=str(input("Introduce una letra o un número por teclado: "))

if var_1.islower()==True:
    print(f"Está en mínusculas la letra {var_1}")
    
elif var_1.isupper()==True:
    print(f"Está en mayúsculas la letra {var_1}")
    
elif var_1.isnumeric()==True:
    print(f"El valor {var_1} que has introducido por teclado es un número")
    
else:
    print(f"¿Es {var_1} un número o una letra?")