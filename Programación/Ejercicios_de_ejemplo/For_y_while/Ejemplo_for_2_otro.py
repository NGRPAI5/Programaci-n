import random

minumero=int(input("Introduce un número: "))
numerosec=random.randint(1,4)

while minumero!=numerosec:
    print("No es igual")
    minumero=int(input("Vuelve a intentarlo: "))
print("Programa finalizado")