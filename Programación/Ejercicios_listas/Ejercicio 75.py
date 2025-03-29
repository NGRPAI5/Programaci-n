#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados:

lista=["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]
numero_valores=0
numeros=0
letras=0
mayusculas=0
suma_numeros=0

for i in lista:
    numero_valores+=1
    
    if i.isnumeric():
        numeros+=1
        suma_numeros+=int(i)
        
    else:
        letras+=1
        
        if i.isupper():
            mayusculas+=1
            
        else:
            mayusculas+=0
            
print("Número de valores:", numero_valores)
print("Cantidad de números:", numeros)
print("Cantidad de letras:", letras)
print("Cantidad de mayúsculas:", mayusculas)
print("Suma total de números:", suma_numeros)
