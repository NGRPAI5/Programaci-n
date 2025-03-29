#9. Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas.

var_1=float(input("Introduce un número de segundos: "))
minutos=var_1/60
horas=minutos/60

print("El número de minutos a partir de los segundos introducidos son:",round(minutos,6),"y el número de horas a partir de los segundos introducidos anteriormente son:",round(horas,6))
