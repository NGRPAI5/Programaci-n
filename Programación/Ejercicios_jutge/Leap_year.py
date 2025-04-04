tiempo = int(input())

if tiempo % 4 == 0:
    if tiempo % 100 != 0:
        print("YES")
    elif tiempo % 400 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")