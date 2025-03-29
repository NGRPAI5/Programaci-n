#19.-Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales.

var_1=int(input("Introduce un número: "))
var_2=int(input("Introduce otro número: "))

if var_1>var_2:
    print(f"El número {var_1} es superior al número {var_2}")

elif var_1<var_2:
    print(f"El número {var_2} es superior al número {var_1}")
    
else:
    print(f"El número {var_1} es igual al número {var_2}")