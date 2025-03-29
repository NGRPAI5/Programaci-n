numero=input("Introduce un número: ")
lista=numero.split(".")

if len(lista)==2:
    if lista[0].isnumeric() and lista[1].isnumeric():
        print("Es un número con decimales")
        
    else:
        print("No es decimal")
        
if len(lista)>2 or len(lista)==1:
    print("No es un número con decimales")