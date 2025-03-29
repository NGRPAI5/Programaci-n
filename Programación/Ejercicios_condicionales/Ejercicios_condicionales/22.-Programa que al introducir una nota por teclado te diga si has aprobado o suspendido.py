#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estÃ¡s aprobado.

var_1=float(input("Introduce una nota: "))

if var_1<0:
    print("La nota que has introducido no está entre 0 y 10")
elif var_1>10:
    print("La nota que has introducido no está entre 0 y 10")

elif var_1>5:
    print(f"Has sacado un {var_1} y estás aprobado")

elif var_1==5:
    print(f"Has sacado un {var_1} y estás aprobado")

else:
    print(f"Has sacado un {var_1} y estás suspendido")
