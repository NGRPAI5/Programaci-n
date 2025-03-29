#El primer ejercicio

#Ha este código le he puesto float para que al introducir un número decimal se puedan sumar.
var_1=float(input("Introduce el primer número: "))

#Le he puesto las comillas para reconocer la pregunta como un texto. Además, le he puesto el float como en la anterior línea de código.
var_2=float(input("Introduce el segundo número: "))

#He anadido un barra baja porqué, las variables no pueden tener espacios. Además, var1 y var2 no eran iguales a las variables de las primeras líneas. Hubiera dado un error.
var_total=var_1+var_2

#Los paréntesis los he cambiad por corchetes, además le he puesto una coma antes de la variable total. Ya por último la variable total la he cambiado por var_total.
print(f"El resultado de sumar {var_1} y {var_2} es:",var_total)
