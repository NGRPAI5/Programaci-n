#1

print("****GASOLINERA****")
print("1. Sin plomo 95")
print("2. Sin plomo 98")
print("3. Gasóleo A")
print("4. Gasóleo A+")
print("******************")

escoger=str(input("Escoja el tipo de combustible:"))


if escoger=="1":
    litros=int(input("Introduzaca el número de litros a repostar: "))
    total_pagar_95=litros*1.765
    print("El total a pagar es:", total_pagar_95)
        
elif escoger=="2":
    litros=int(input("Introduzaca el número de litros a repostar: "))
    total_pagar_98=litros*1.913
    descuento=total_pagar_98-(total_pagar_98/100*10)
    print(f"El total a pagar es de {total_pagar_98} y con el descuento queda en {descuento}")
    
elif escoger=="3":
    litros=int(input("Introduzaca el número de litros a repostar: "))
    total_pagar_A=(litros*1.746)
    print("El total a pagar es:", total_pagar_A)
        
elif escoger=="4":
    litros=int(input("Introduzaca el número de litros a repostar: "))
    total_pagar_AA=(litros*1.839)
    descuento_A=total_pagar_AA-(total_pagar_AA/100*12)
    print(f"El total a pagar es de {total_pagar_AA} y con el descuento queda en {descuento_A}")
    