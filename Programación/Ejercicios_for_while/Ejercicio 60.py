#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while.

numero=int(input("Introduce un número para hacer su tabla de multiplicar: "))
numero_multiplicador=1
total=0

while numero_multiplicador<11:
    total=numero*numero_multiplicador
    print(f"Si multiplicamos {numero} por {numero_multiplicador} nos da {total}")
    numero_multiplicador+=1
