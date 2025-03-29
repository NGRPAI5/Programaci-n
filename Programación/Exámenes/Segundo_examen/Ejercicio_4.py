#4

var_min=int(input("Introduce el valor mínimo:"))
var_max=int(input("Introduce el valor máximo:"))
var_intervalo=int(input("Introduce el intervalo:"))
resultado=0
rang=int(var_max/var_intervalo)

for i in range(rang):
    resultado=(var_min+var_intervalo)+resultado
    print(resultado, end="")
    
print(resultado)

