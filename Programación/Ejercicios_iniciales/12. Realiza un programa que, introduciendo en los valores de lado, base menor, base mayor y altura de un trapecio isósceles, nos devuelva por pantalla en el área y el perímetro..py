#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla el área y el perímetro.

var_1=float(input("Introduce el valor del lado: "))
var_2=float(input("Introduce el valor de la base menor: "))
var_3=float(input("Introduce el valor del la base mayor: "))
var_4=float(input("Introduce el valor de la altura del trapecio isósceles: "))
perimetro=var_1+var_2+var_3+var_4
area=(var_2+var_3)/2*var_4

print("El períetro del trapecio isósceles es de: ",perimetro)
print("El área del trapecio isósceles es de: ",area)
