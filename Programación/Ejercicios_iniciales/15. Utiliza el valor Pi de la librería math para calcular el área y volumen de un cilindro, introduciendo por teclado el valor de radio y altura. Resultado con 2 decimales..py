#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math

var_1=float(input("Introduce el valor del radio del cilindro: "))
var_2=float(input("Introduce el valor de la altura del cilindro: "))
volumen=math.pi*var_1**2*var_2
area=2*math.pi*var_1*var_2+2*math.pi*var_1**2

print("El resultado del volumen a partir del radio y la altura es de:",round(volumen,2))
print("El resultado del área a partir del radio y la altura es de:",round(area,2))
