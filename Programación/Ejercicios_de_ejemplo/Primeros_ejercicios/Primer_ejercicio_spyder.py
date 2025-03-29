print("1.-Cars")
print("2.-Cars 2")
print("3.-Cars 3")
print("4.-Ford vs Ferrari")
print("5.-Lamborghini")
print("6.-Ferrari")

var_menu=int(input("Introduce una opción: "))

#Tres opciones para mostrar en pantalla error si el número no está entre 1 y 4
if var_menu<1 or var_menu>6:
#if var_menu>=1 and var_menu<=4:
    print("Error")
    
else:
    

    if var_menu==1 or var_menu==4 or var_menu==5 or var_menu==6:
        print("El precio es de 10 euros")
    
    if var_menu==2:
        print("El precio es de 12 euros")
    
    if var_menu==3:
        print("El precio es de 14 euros")
        
print("Programa finalizado")
    

#Otra forma con if, elif y else
"""
    if var_menu==1 or var_menu==4:
        print("El precio es de 10 euros")
    
    elif var_menu==2:
        print("El precio es de 12 euros")
    
    elif var_menu==3:
        print("El precio es de 14 euros")
        
    else:
        print("Error")
        
print("Programa finalizado")
"""