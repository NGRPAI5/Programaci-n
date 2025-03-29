#Juego 7,5 Fase 2

import random

acumulado=0
deposito=100

print("Bienvenido al juego del 7 y medio.")

while deposito > 0:
    carta=str(input("¿Quieres carta? s/n: "))
    
    if carta == "s":
        numero=random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
        print("Tu carta es:", numero)
        
        if numero>7:
            valor=0.5
        else:
            valor=numero
            
        acumulado+=valor
           
        print("Tu acumulado es de:", acumulado)
        
        if acumulado > 7.5:
            print("¡Has perdido la partida!")
            deposito-=10
            acumulado=0
            print("Tu depósito es de:", deposito)
            
            if deposito <= 0:
                print("Te has quedado sin puntos. No puedes continuar jugando.")
                deposito=0
                        
            else:
                jugar=str(input("¿Quieres jugar una nueva partida? s/n: "))
                if jugar != "s":
                    print("Gracias por jugar. Tu depósito final es:", deposito)
                    deposito=0
            
        elif acumulado == 7.5:
            print("Enhorabuena, has ganado la partida.")
            deposito+=10
            acumulado=0
            print("Tu depósito es de:", deposito)
            
            jugar=str(input("¿Quieres jugar una nueva partida? s/n: "))
            
            if jugar != "s":
                print("Gracias por jugar. Tu depósito final es:", deposito)
                deposito=0
    
    else:
        print("Te plantas con un acumulado de:", acumulado)

        if acumulado < 6:
            print("Quizás tendrías que arriesgar un poco ¿no?")
            acumulado=0
            deposito-=5
                
        elif acumulado <= 7:
            print("Has sido un poco conservador")
            acumulado=0
            deposito+=5
        
        acumulado = 0
        
        print("Tu depósito actual es de:", deposito)
        jugar = input("¿Quieres jugar una nueva partida? s/n: ")
        if jugar != "s":
            print("Gracias por jugar. Tu depósito final es:", deposito)
            deposito=0