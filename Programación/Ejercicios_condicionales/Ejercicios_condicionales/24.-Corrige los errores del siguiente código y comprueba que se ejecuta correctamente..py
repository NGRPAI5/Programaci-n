#24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente.

var_1=float(input("Introduce el peso: "))
var_2=float(input("Introduce la altura: "))

var_imc=var_1/var_2**2

print(f"Si pesas {var_1} kilos y mides {var_2} metros, tu IMC es de:",round(var_imc,2))

if var_imc>25:
    print("Tienes sobrepeso")

else:
    print("Estás dentro de los parámetros normales")