intervalos=input().split()

a_1=int(intervalos[0])
a_2=int(intervalos[2])
b_1=int(intervalos[1])
b_2=int(intervalos[3])

if a_1==a_2 and b_1==b_2:
    print("=")
    
elif a_1>=a_2 and b_1<=b_2:
    print("1")
    
elif a_1<=a_2 and b_1>=b_2:
    print("2")
    
else:
    print("?")
