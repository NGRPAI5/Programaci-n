#20.-A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclado nÃºmeros entre 0 y 10

var_1=int(input("Introduce un nœmero: "))
var_2=int(input("Introduce otro nœmero: "))

if var_1>10 or var_1<(-1):
    print("Uno o los dos nœmeros est‡n fuera de los l’mites establecidos")
    
elif var_2>10 or var_1<(-1):
    print("Uno o los dos nœmeros est‡n fuera de los l’mites establecidos")
    
else:

    if var_1>var_2:
        print(f"El nœmero {var_1} es superior al nœmero {var_2}")

    elif var_1<var_2:
        print(f"El nœmero {var_2} es superior al nœmero {var_1}")
    
    else:
        print(f"El nœmero {var_1} es igual al nœmero {var_2}")

