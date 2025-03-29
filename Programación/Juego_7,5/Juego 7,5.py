#Juego 7,5 Fase 1

import random

continuar=True
acumulado=0

print("Bienvenido al juego del 7 y medio.")

while continuar == True:
    
    carta=str(input("¿Quieres carta?: s/n "))
    
    if carta != "S" and carta != "s":
        continuar=False
    
    else:    
        numero=random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
        print("Tu carta es:", numero)
        
        if numero>7:
            valor=0.5
        else:
            valor=numero
            
        acumulado+=valor
           
        print("Tu acumulado es de:", acumulado)
        
        if acumulado > 7.5:
            print("Has perdido la partida!")
            continuar=False
            
        elif acumulado == 7.5:
            print("Enhorabuena, has ganado la partida.")
            continuar=False
        
if acumulado < 6:
    print("Quizás tendrías que arriesgar un poco ¿no?")
    continuar=False
    
elif acumulado <= 7:
    print("Has sido un poco conservador")
    continuar=False
    