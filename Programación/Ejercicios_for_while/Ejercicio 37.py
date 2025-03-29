#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

notas=int(input("Introduce el número de notas que quieres poner: "))

for i in range(notas):
    calificacion=float(input("Introduce tu calificación: "))
    
    if calificacion >= 5:
        print("Asignatura aprobada")
        
    else:
        print("Asignatira suspendida")