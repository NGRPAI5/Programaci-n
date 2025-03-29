#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos.

import numpy as np

ingles=[]
castellano=[]
catalan=[]

ingles_nota=0
castellano_nota=0
catalan_nota=0
media_ingles=0
media_castellano=0
media_catalan=0
mediana_ingles=0
mediana_castellano=0
mediana_catalan=0

repetir=True

while repetir==True:
    estudiante=str(input("Introduce el nombre del estudiante: "))
    
    ingles_nota=float(input("Introduce una nota de inglés: "))
    castellano_nota=float(input("Introduce una nota de castellano: "))
    catalan_nota=float(input("Introduce una nota de catalán: "))
    
    ingles.append(ingles_nota)
    castellano.append(castellano_nota)
    catalan.append(catalan_nota)
        
    preguntar=str(input("¿Quieres repetir s/n?: "))
    
    if preguntar=="s" or preguntar=="S":
        repetir=True
        
    else:
        repetir=False
    
media_ingles=np.mean(ingles)
media_castellano=np.mean(castellano)
media_catalan=np.mean(catalan)

mediana_ingles=np.median(ingles)
mediana_castellano=np.median(castellano)
mediana_catalan=np.median(catalan)

print("La media de inglés es de:", round(media_ingles, 2))
print("La media de castellano es de:", round(media_castellano, 2))
print("La media de catalán es de:", round(media_catalan, 2))
print("La mediana de inglés es de:", round(mediana_ingles, 2))
print("La mediana de castellano es de:", round(mediana_castellano, 2))
print("La mediana de catlán es de:", round(mediana_catalan, 2))
