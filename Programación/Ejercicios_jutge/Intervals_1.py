intervalos=input().split()

a_1=int(intervalos[0])
a_2=int(intervalos[2])
b_1=int(intervalos[1])
b_2=int(intervalos[3])

inicio=max(a_1, a_2)
fin=min(b_1, b_2)

if inicio <= fin:
    print(f"[{inicio},{fin}]")
    
else:
    print("[]")
