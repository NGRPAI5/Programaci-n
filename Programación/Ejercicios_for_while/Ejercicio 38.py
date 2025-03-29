#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10.

notas=int(input("Introduce el número de notas que quieres poner: "))

for i in range(notas):
    calificacion=float(input("Introduce tu calificación: "))
    
    if 0 <= calificacion <= 10:
    
        if calificacion >= 5:
            print("Asignatura aprobada")
        
        else:
            print("Asignatura suspendida")
            
    else:
        print("Has introducido una nota equivocada.")
