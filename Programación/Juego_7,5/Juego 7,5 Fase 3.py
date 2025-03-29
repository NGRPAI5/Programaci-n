#Juego 7,5 Fase 3

alias_mayus=str(input("Introduce un nombre: ")).lower().capitalize()

import random

valor=0
acumulado=0
banca=False
resultado_A=0
resultado_B=0
repetir=True
entrada=False

print("Bienvenido al juego del 7 y medio", alias_mayus)
print("**********************************************************")

while repetir==True:
    while banca==False:
        carta=str(input(f"¿Quieres carta {alias_mayus}? s/n: "))
        
        if carta == "s":
            numero=random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
            print(f"{alias_mayus}, tu carta es: {numero}")
            
            if numero>7:
                valor=0.5
            else:
                valor=numero
                
            acumulado+=valor
               
            print(f"{alias_mayus}, tu acumulado es de: {acumulado}")
            
            if acumulado > 7.5:
                print(f"¡Has perdido la partida {alias_mayus}.")
                resultado_A=-1
                acumulado=0
                break
                
            elif acumulado == 7.5:
                print(f"Enhorabuena {alias_mayus}, has ganado la partida.")
                resultado_A+=acumulado
                acumulado=0
                break
        
        elif carta == "n":
            print(f"{alias_mayus} te plantas con un acumulado de: {acumulado}.")
            
            if acumulado < 6:
                print(f"¿Quizás tendrías que arriesgar un poco no, {alias_mayus}. Ahora es el turno es de la BANCA?")
                resultado_A+=acumulado
                acumulado=0
                banca=True
                    
            elif acumulado <= 7:
                print(f"Has sido un poco conservador, {alias_mayus}. Ahora es el turno es de la BANCA")
                resultado_A+=acumulado
                acumulado=0
                banca=True
                
        else:
            print("Entrada inválida. Inténtelo de nuevo")
                
    while banca==True:
            input("TURNO DE LA BANCA. Pulsa enter para visualizar carta a carta")
            
            if acumulado < 5.5:
                numero=random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
                
                if numero>7:
                    valor=0.5
                else:
                    valor=numero
                    
                acumulado+=valor
                
                input(f"La banca ha sacado la carta: {numero}")
                input(f"La banca acumula: {acumulado}")
                
            else:
                input("La Banca se ha plantado")
                resultado_B+=acumulado
                acumulado=0
                banca=False
            
            if acumulado > 7.5:
                input("La BANCA ha perdido la partida.")
                resultado_B+=0
                acumulado=0
                banca=False
                
            elif acumulado == 7.5:
                input("La BANCA ha ganado la partida.")
                resultado_B+=acumulado
                acumulado=0
                banca=False
                
    if resultado_A > resultado_B:
        print(f"Ha ganado {alias_mayus}.")
        
    elif resultado_A == resultado_B:
        print("Ha sido un empate")
        
    else:
        print("Ha ganado la BANCA")
        
    print("**********************************************************")
       
    while True:
        carta=str(input(f"¿Quieres jugar {alias_mayus}? s/n: "))
         
        if carta == "s":
            repetir=True
            valor=0
            acumulado=0
            resultado_A=0
            resultado_B=0 
            break
             
        elif carta == "n":
            repetir=False
            break
            
        else:
            print("Entrada inválida. Inténtelo de nuevo")
