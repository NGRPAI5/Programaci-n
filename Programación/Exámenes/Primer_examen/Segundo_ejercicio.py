#El segundo ejercicio.

#Definimos las dos variables. En estas almacenaremos los dos números que preguntaremos.
var_1=float(input("Introduce el primer número: "))
var_2=float(input("Introduce el segundo número: "))

#Además, he creado la variable var_total para que sume los dos números introducidos por teclado.
var_total=var_1+var_2
#Después, he definido esta otra variable por si, en un fututo se quisiera cambiar el número por el cual se divide var_total.
numero_division=3
#Por último, esta variable sirve para poder dividir la suma de los dos números entre el número que quisimos poner de dividendo.
var_division=var_total/numero_division

#En estos prints, mostramos por pantalla la suma de var_1+var_2 y en el otro mostramos la división de var_total entre numero_division. También hay puesto un round que redondea a 3 decimales.
print(f"El resultado de sumar {var_1} y {var_2} es:",var_total)
print(f"El resultado de dividir {var_total} entre {numero_division} es:",round(var_division,3))
