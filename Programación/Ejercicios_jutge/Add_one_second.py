preguntar=input()

lista=preguntar.split()
horas=int(lista[0])
minutos=int(lista[1])
segundos=int(lista[2])

segundos+=1

if segundos == 60:
    segundos=0
    minutos+=1
    
    if minutos == 60:
        minutos=0
        horas+=1
        
        if horas == 24:
            segundos=0
            minutos=0
            horas=0
        
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")