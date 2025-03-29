temperatura=int(input())

if temperatura >= 100:
    print("it's hot")
    print("water would boil")
    
elif temperatura > 30:
    print("it's hot")
    
elif temperatura >= 10:
    print("it's ok")

elif temperatura <= 0:
    print("it's cold")
    print("water would freeze")
    
else:
    print("it's cold")