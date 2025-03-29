#Password versió 2

print("1.-La longitud de la contraseña tiene que tener entre 6 y 8 caracteres")
print("2.-Forçar los siguinetes valores según la posición indicada:")
print("    Posición 1: Un número mayor o igual a 1 i menor o igual a 5.")
print("    Posición 2: Una letra en minúscula.")
print("    Posición 3: Una letra en mayúscula.")
print("    Posición 4: Uno de los siguinetes símbolos *, _, @")
print("    Posición 5: Una letra minúscula.")
print("    Posición 6: Un número mayor o igual a 6 i menor o igual a 9.")
print("    Posición 7: Uno de los siguinetes símbolos &, /, #")
print("    Posición 8: Un número menor o igual que 5.")

password_correcto=0
password_incorrecto=0
numero_entre_1_3=False
numero_entre_4_6=False
numero_entre_7_9=False
minuscula=False
mayuscula=False
simbolo_1=False
simbolo_2=False

password=str(input("Introduce la contraseña: "))

if len(password) < 6 or len(password) > 8:
    print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos.")
        
else:
    for j in password:
        if j.isdigit():
            numero=int(j)
            if 1 <= numero <= 3:
                numero_entre_1_3=True
                
            if 4 <= numero <= 6:
                numero_entre_4_6=True
                
            if 7 <= numero<= 9:
                numero_entre_7_9=True
                
        elif j.islower():
            minuscula=True
            
        elif j.isupper():
            mayuscula=True
            
        elif j in "*_@":
            simbolo_1=True
            
        elif j in "&/#":
            simbolo_2=True
                
if (numero_entre_1_3 and numero_entre_4_6 and numero_entre_7_9 and minuscula and mayuscula and simbolo_1 and simbolo_2):
    print("Cumple los requisitos")
    
else:
    print("La contraseña no cumple:")
    
    if not numero_entre_1_3:
        print("La contraseña no tiene un número entre un 1 y un 3.")
        
    if not numero_entre_4_6:
        print("La contraseña no tiene un número entre un 4 y un 6.")
        
    if not numero_entre_7_9:
        print("La contraseña no tiene un número entre un 7 y un 9. ")
        
    if not minuscula:
        print("La contraseña no tiene minúscula.")
        
    if not mayuscula:
        print("La contraseña no tiene mayúscula.")
        
    if not simbolo_1:
        print("La contraseña no tiene simbolo.")
        
    if not simbolo_2:
        print("La contraseña no tiene otro simbolo.")
                