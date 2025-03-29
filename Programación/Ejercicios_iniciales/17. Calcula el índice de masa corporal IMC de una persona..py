#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

var_1=float(input("Introduce el valor de tú peso: "))
var_2=float(input("Introduce el valor de tú altura: "))
imc=var_1/(var_2**2)

if imc>25:
    print("Tienes sobrepeso","tú IMC es de:",round(imc,2))
elif imc==25:
    print("Tienes sobrepeso","tú IMC es de:",round(imc,2))
else:
    print("No tienes sobrepeso","tú IMC es de:",round(imc,2))
