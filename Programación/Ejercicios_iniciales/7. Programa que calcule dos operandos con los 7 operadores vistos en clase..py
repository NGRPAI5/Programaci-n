#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

var_1=int(input("Introduce un número: "))
var_2=int(input("Introduce un segundo número: "))
suma=var_1+var_2
resta=var_1-var_2
multiplicacion=var_1*var_2
division=var_1/var_2
exponente=var_1**var_2
division_entera=var_1//var_2
operador_modulo=var_1%var_2


print("La suma de operador1 y operador2 es: ",suma)
print("La resta de operador1 y operador2 es: ",resta)
print("La multiplicación de operador1 y operador2 es: ",multiplicacion)
print("La división de operador1 y operador2 es: ",round(division,2))
print("El exponente de operador1 y operador2 es: ",exponente)
print("La division entera de operador1 y operador2 es:",division_entera)
print("El operador del módulo de operador1 y operador2 es:",operador_modulo)





