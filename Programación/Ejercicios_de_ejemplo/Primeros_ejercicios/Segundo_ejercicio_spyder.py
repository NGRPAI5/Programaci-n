precio_1=9
precio_2=13
precio_3=12

print("1.-Cars")
print("2.-Cars 2")
print("3.-Cars 3")
print("4.-Ford vs Ferrari")
print("5.-Lamborghini")
print("6.-Ferrari")


var_menu=input("Introduce una opción: ")

if var_menu.isnumeric()==True:
    print("Es un número")
else:
    print("No es un número")
    

if var_menu=="1" or var_menu=="4" or var_menu=="5" or var_menu=="6":
    print("El precio es",precio_1,"euros")
    
elif var_menu=="2":
    print(f"El precio es {precio_2} euros")
    
elif var_menu=="3":
    print(f"El precio es {precio_3} euros")
        
else:
    print("Error")
    
print("Fin del programa")