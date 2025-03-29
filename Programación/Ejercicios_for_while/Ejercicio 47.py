#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida.

primer_intervalo=int(input("Introduce un primer intervalo: "))
segundo_intervalo=int(input("Introduce un segundo intervalo: "))
intervalo_augmento=primer_intervalo
resta=primer_intervalo-segundo_intervalo

if primer_intervalo<segundo_intervalo:
    print(primer_intervalo, end="-")
    for i in range(primer_intervalo, segundo_intervalo-1):
        intervalo_augmento+=1
        print(intervalo_augmento, end="-")
    print(segundo_intervalo, end="")
    
else:
    print(primer_intervalo, end="-")
    for i in range(primer_intervalo - 1, segundo_intervalo, -1):
        print(i, end="-")
    print(segundo_intervalo)