#Definición de tres tipos distintos de variables

var_entero=4
var_dec=3.5
var_text="hola"

print(var_entero)
print(var_dec)
print(var_text)

#Maneras de visualizar la información de salida

#Manera 1 añadir texto entre comillas, separando con comas la variable
print("El resultado es:",var_entero,"manzanas")

var_total=var_entero*var_dec

#Otra manera de print, con formato
print(f"El resultado de sumar {var_entero} * {var_dec} es: ",var_total)
