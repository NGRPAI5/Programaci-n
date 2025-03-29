a_b=input()
division=0
resto=0

lista=a_b.split()
numeros=[int(num) for num in lista]

division=numeros[0]//numeros[1]
resto=numeros[0]-(division*numeros[1])

print(f"{division} {resto}")