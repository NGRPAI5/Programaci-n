#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While

buenos_dias=0
numero_veces=int(input("Introduce el número de veces que quieras que se vea la frase Buenos días: "))

while buenos_dias<numero_veces:
    print("¡Buenos días!")
    buenos_dias+=1
    