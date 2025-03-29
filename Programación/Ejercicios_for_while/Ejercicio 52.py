#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While

repeticion=True

while repeticion==True:
    var_1=int(input("Introduce un número entero: "))
    var_2=int(input("Introduce un segundo número entero: "))
    suma=var_1+var_2
    print("La suma del primer número y el segundo es de:",suma)
    
    repetir=str(input("Quieres repetir s/n: "))
    
    if repetir=="s":
        repeticion=True
        
    else:
        repeticion=False
        print("Programa finalizado.")
    