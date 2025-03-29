#3

cifras=int(input("Introduce el número de cifras: "))
el_numero=int(input("Introduce el número: "))
suma=0
posicion=0

for i in range(cifras):
    suma=suma+el_numero[posicion]
    posicion+=1
    
print(suma)
    