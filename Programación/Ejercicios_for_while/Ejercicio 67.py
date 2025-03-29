#67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes consideraciones.

print("Debe tener una longitud entre 6 y 8 caracteres.")
print("Debe contener como mínimo:")
print("2 números mayores o iguales que 1 y menor o igual que 5")
print("2 letras minúsculas")
print("1 letra mayúscula")
print("2 símbolos (*, _, @, &,/,#)")
print("1 número mayor o igual que 6 y menor o igual que 5")

numeros=0
minusculas=0
mayusculas=0
simbolos=0
correcto=0

password=str(input("Introduce una contraseña: "))

while len(password) > 6 or len(password) < 8:
    for i in password:
            if i.islower():
                minusculas+=1
                
            elif i.isupper():
                mayusculas+=1
                
            elif i == "*_@&/#":
                simbolos+=1
                
            else:
                numeros+=1
                
            if minusculas == 2:
                correcto+=1
                
            if mayusculas == 1:
                correcto+=1
                
            if simbolos == 2:
                correcto+=1
                
            if numeros == 3:
                correcto+=1
                
            else:
                print("Password incorrecta")

print("Password incorrecta")

