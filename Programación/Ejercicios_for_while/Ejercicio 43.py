#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra.

palabra=str(input("Introduce una palabra: "))
posicion=0

for i in palabra:
    print(f"En la posición {posicion} está la {i}")
    posicion+=1
    