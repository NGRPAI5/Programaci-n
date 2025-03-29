numeros = []
numeros_2=[]

while len(numeros) < 3:
    numeros.extend(input().split())
    
for i in numeros:
    numeros_2.append(int(i))
    
suma=sum(numeros_2)
print(suma)