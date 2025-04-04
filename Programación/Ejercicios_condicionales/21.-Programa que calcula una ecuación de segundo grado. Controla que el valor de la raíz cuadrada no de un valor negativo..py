#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo.
import math

var_1=float(input("Introduce el valor para la A de la ecuación de segundo grado: "))
var_2=float(input("Introduce el segundo valor para la B de la ecuación de segundo grado: "))
var_3=float(input("Introduce el tercer valor para la C de la ecuación de segundo grado: "))

total=var_2**2-4*var_1*var_3

if total<0:
    print("La raíz no puede ser un valor negativo")
    
elif total==0:
    una_solucion=-var_2/2*var_1
    print("Hay una solución",una_solucion)

else:
    formula_1=(-var_2+math.sqrt(total))/2*var_1
    formula_2=(-var_2-math.sqrt(total))/2*var_1
    
    print("El valor de x1 es igual a:",formula_1)
    print("El valor de x2 es igual a:",formula_2)

