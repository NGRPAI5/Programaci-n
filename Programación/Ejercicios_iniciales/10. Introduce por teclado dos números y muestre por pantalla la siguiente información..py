#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

var_1=float(input("Introduce un número por teclado: "))
var_2=float(input("Introduce otro número por teclado: "))
division=var_1/var_2
resto=var_1%var_2

if var_1%2==0:
    print("El número es par")
else:
    print("El número es impar")


print("El resultado del cociente es:",division)
print("El resto de la división es:",resto)
