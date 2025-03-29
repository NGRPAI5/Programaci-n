tiempo=int(input())

horas=tiempo//3600
segundos=tiempo%3600
minutos=segundos//60
segundos_2=segundos%60

print(horas, minutos, segundos_2)