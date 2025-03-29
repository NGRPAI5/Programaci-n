#68. Añade al ejercicio anterior la posibilidad de que el programa pregunte si deseas o no continuar introduciendo passwords. Ej. “¿Deseas introducir otro password s/n?

print("La longitud de la contraseña debe tener entre 6 y 8 caracteres.")
print("Debe contener como mínimo:")
print("    Debe tener 2 números mayores o iguales que 1 y menor o igual que 5")
print("    Debe tener 2 letras minúsculas")
print("    Debe tener 1 letra mayúscula")
print("    Debe tener 2 símbolos (*, _, @, &,/,#)")
print("    Debe tener 1 número mayor o igual que 6 y menor o igual que 5")

password_correcto=0
password_incorrecto=0
numeros_1_5=0
numeros_6_9=0
minusculas=0
mayusculas=0
simbolos=0
continuar=True

while continuar == True:
    password=str(input("Introduce la contraseña: "))
    
    if len(password) < 6 or len(password) > 8:
        print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos.")
            
    else:
        for j in password:
            if j.isdigit():
                numero=int(j)
                if 1 <= numero <= 5:
                    numeros_1_5+=1
                    
                if 6 <= numero <= 9:
                    numeros_6_9+=1
                    
            elif j.islower():
                minusculas+=1
                
            elif j.isupper():
                mayusculas+=1
                
            elif j in "*_@&/#":
                simbolos+=1
                
    if numeros_1_5 == 2:
        if numeros_6_9 == 1:
            if minusculas == 2:
                if mayusculas == 1:
                    if simbolos == 2:
                        print("Password correcto")
            
    else:
        print("La contraseña es incorrecta")
        
    pregunta=str(input("Deseas repetir la contraseña (s/n): "))
    
    if pregunta == "s" or pregunta == "S":
        continuar=True
        
    else:
        continuar=False
