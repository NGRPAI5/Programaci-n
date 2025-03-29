#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural. Con While

suma_total=0
repeticiones=0
repeticion=True

while repeticion==True:
    var_1=int(input("Introduce un número entero: "))
    var_2=int(input("Introduce un segundo número entero: "))
    suma=var_1+var_2
    suma_total+=suma
    repeticiones+=1
    print("La suma del primer número y el segundo es de:",suma)
    print("La suma total es de:", suma_total)
    if repeticiones==1:
        print(f"Llevas {repeticiones} operación realizada.")
        
    else:
        print(f"Llevas {repeticiones} operaciones realizadas.")
    
    if suma_total>50:
        repetir=str(input("Quieres repetir s/n: "))
        
        if repetir=="s":
            repeticion=True
            
        else:
            repeticion=False
        
    else:
        repeticion==True
    
print("Resumen: ")    
print("La suma total de los número puestos son de:", suma_total)
print("El número de repeticiones que has hecho son de:", repeticiones)
print("Programa finalizado.")
