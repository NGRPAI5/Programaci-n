#Cuarto ejercicio.

#Definimos las dos variables para que pidan los dos números y se introduzcan por teclado.
var_1=int(input("Introduce un primer número: "))
var_2=int(input("Introduce un segundo número: "))

#Definimos las tres variables para los tres operadores división entera, esponente y modulo. Éstos utilizarán los dos números introducidos anteriormente.
division_entera=var_1//var_2
exponente=var_1**var_2
modulo=var_1%var_2

#Para acabar, los prints mostrarán por pantalla el resultado de los tres operadores.
print(f"El resultado de {var_1} y {var_2} en la división entera es de:",division_entera)
print(f"El resultado de {var_1} y {var_2} en el exponente es de:",exponente)
print(f"El resultado de {var_1} y {var_2} en el módulo es de:",modulo)
