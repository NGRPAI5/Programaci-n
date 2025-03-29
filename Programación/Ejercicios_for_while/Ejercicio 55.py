#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

suma_total=0
repeticiones=0
repetir=True

while repetir==True:
    var_1=int(input("Introduce un número entero: "))
    var_2=int(input("Introduce un segundo número entero: "))
    suma=var_1+var_2
    suma_total+=suma
    repeticiones+=1
    print("La suma del primer número y el segundo es de:",suma)
    if repeticiones==1:
        print(f"El total acumulado es de {suma_total} y llevas {repeticiones} operación realizada.")
        
    else:
        print(f"El total acumulado es de {suma_total} y llevas {repeticiones} operaciones realizadas.")
    
    if suma_total<50 or suma_total % 2 == 0:
        repetir=True
        
    else:
        repetir=False

print("Resumen: ")    
print("La suma total de los número puestos son de:", suma_total)
print("El número de repeticiones que has hecho son de:", repeticiones)
print("Programa finalizado.")
