#Password versión 1

#Muestro por pantalla las siguientes instrucciones.
print("1.-La longitud de la contraseña tiene que tener entre 6 y 8 caracteres.")
print("2.-Forzar los siguientes valores según la posición indicada:")
print("    Posición 1: Un número mayor o igual a 1 y menor o igual a 5.")
print("    Posición 2: Una letra en minúscula.")
print("    Posición 3: Una letra en mayúscula.")
print("    Posición 4: Uno de los siguinetes sí­mbolos *, _, @")
print("    Posición 5: Una letra minúscula.")
print("    Posición 6: Un número mayor o igual a 6 y menor o igual a 9.")
print("    Posición 7: Uno de los siguientes sí­mbolos &, /, #")
print("    Posición 8: Un número menor o igual que 5.")

#Creo una variable password que pregunte por una contraseña. Además creo otra que empieza en False para luego poder mostrar que la contraseña es correcta si sigue siendo False.
password=str(input("Introduce la contraseña: "))
error=False

#Calculo la longitud del password y miro si es igual o más grande que 6 o igual o más pequeño que 8. Por último, si hay error que la variable sea True.
if len(password) < 6 or len(password) > 8:
    print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos.")
    error = True

#Si no fallase la longitud del password, es decir que está comprendida entre 6 y 8, que compruebe lo siguiente:    
else:
    
    #Si el primer dígito no es igual o superior a 1 o igual o inferior a 5, que muestre un print diciendo error.
    if not 1 <= int(password[0]) <= 5:
        print("Error en el caracter 1. ", end="")
        error = True
        
    #Si el segundo dígito no es minúscula, que muestre un print diciendo error.
    if not password[1].islower():
        print("Error en el caracter 2. ", end="")
        error = True
        
    #Si el tercer dígito no es mayúscula, que muestre un print diciendo error.
    if not password[2].isupper():
        print("Error en el caracter 3. ", end="")
        error = True
    
    #Si el cuarto dígito no es *, _, @, que muestre un print diciendo error.
    if password[3] not in "*_@":
        print("Error en el caracter 4. ", end="")
        error = True
    
    #Si el quinto dígito no es minúscula, que muestre un print diciendo error.
    if not password[4].islower():
        print("Error en el caracter 5. ", end="")
        error = True
    
    #Si el sexto dígito no está comprendido entre el rango de 6 y 9, que muestre un print diciendo error.
    if not 6 <= int(password[5]) <= 9:
        print("Error en el caracter 6. ", end="")
        error = True
        
    #Si la contraseña del password es superior a los 6 dígitos, que prosiga con el siguiente print. De esta forma no salta error en la consola.
    if len(password) > 6:    
        #Si el séptimo dígito no tiene &, /, #, que diga error en la consola.
        if password[6] not in "&/#":
            print("Error en el caracter 7. ", end="")
            error = True
    
    #Si la contraseña del password es superior a los 7 dígitos, que prosiga con el siguiente print. De esta forma no salta error.
    if len(password) > 7:
        #Si el séptimo dígito no es superior a 5 o igual, que diga error.
        if not int(password[7]) < 5:
            print("Error en el caracter 8. ", end="")
            error = True

#Para acabar, si error no es True que muestre por pantalla que la contraseña es correcta.        
if not error:
    print("El formato de password es correcto.")
