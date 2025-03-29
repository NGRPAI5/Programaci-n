#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While

suma_total=0
repeticiones=1

while repeticion!=True:
    var_1=int(input("Introduce un número entero: "))
    var_2=int(input("Introduce un segundo número entero: "))
    suma=var_1+var_2
    suma_total+=suma
    print("La suma del primer número y el segundo es de:",suma)
    
    repetir=str(input("Quieres repetir s/n: "))
    
    if repetir=="s":
        repeticion==True
        repeticiones+=1
        
    else:
        print("Programa finalizado.")
        break
    
print("Resumen: ")    
print("La suma total de los número puestos son de:", suma_total)
print("El número de repeticiones que has hecho son de:", repeticiones)