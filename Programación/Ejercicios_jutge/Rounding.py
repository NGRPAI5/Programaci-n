import math

numeros=float(input())

numero_abajo=math.floor(numeros)
numero_arriba=math.ceil(numeros)
if numeros % 1 == 0.5:
    redondeo = math.ceil(numeros)  # Redondear hacia arriba
else:
    redondeo = round(numeros)

print(f"{numero_abajo} {numero_arriba} {redondeo}")