#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

n=int(input("Introduce un número natural: "))
suma=0

for numeros in range(1, n+1):
    suma=suma+numeros
    
print(f"La suma total de números naturales es: {suma}")