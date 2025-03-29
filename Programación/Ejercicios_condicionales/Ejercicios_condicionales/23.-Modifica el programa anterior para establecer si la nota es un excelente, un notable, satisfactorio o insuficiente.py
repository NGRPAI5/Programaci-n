#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

var_1=float(input("Introduce una nota: "))

if var_1<0:
    print("Introduce una nota entre el 0 y el 10")

elif var_1>10:
    print("Introduce una nota entre el 0 y el 10")
    
elif var_1>=8.5:
    print(f"Tu nota es un {var_1}, has sacado un logro excelente")

elif var_1>=6.5:
    print(f"Tu nota es un {var_1}, has sacado un logro notable")
    
elif var_1>=5:
    print(f"Tu nota es un {var_1}, has sacado un logro satisfactorio")

else:
    print(f"Tu nota es un {var_1}, has sacado un logro insuficiente")
