#Tercer ejercicio.

#Importamos la librería math para poder hacer la raíz cuadrada.
import math

#Definimos la variable var_1 de tipo float para poder introducir cualquier número decimal que tenga el triángulo.
var_1=float(input("Introduce el valor de uno de los lados del triángulo equilátero: "))

#Después, definimos la variable area para poder calcular el area a partir del valor 1.
area=(math.sqrt(3)/4)*var_1**2

#Para acabar, el print mostrará el resultado del área del triángulo equilátero y, además lo redondeará a dos decimales.
print("El resultado de el área del triángulo equilátero es de:",round(area,2))
