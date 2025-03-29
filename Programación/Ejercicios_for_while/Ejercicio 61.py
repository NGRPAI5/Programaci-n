#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.

numero=int(input("Introduce un número para hacer su tabla de multiplicar: "))
numero_multiplicador=1
total=0

while total<40:
    total=numero*numero_multiplicador
    print(f"Si multiplicamos {numero} por {numero_multiplicador} nos da {total}")
    numero_multiplicador+=1

print("Fin de programa.")
