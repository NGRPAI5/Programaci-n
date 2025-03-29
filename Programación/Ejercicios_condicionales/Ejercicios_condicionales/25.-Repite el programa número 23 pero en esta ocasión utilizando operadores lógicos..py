#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

var_1=float(input("Introduce una nota: "))

if var_1<0 or var_1>10:
    print("Introduce una nota entre el 0 y el 10")
    
elif var_1>=8.5:
    print(f"Tú nota es un {var_1}, has sacado un logro excelente")

elif var_1>=6.5:
    print(f"Tú nota es un {var_1}, has sacado un logro notable")
    
elif var_1>=5:
    print(f"Tú nota es un {var_1}, has sacado un logro satisfactorio")

else:
    print(f"Tú nota es un {var_1}, has sacado un logro insuficiente")