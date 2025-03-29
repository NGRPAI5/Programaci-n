#56. Realiza un programa que gestione un establecimiento de venta de bocadillos.

print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")

continuar=True

menu=0
acompanamineto=0
bebidas=0

pedidos=0
total_pagar=0
total_pagar_iva=0
total_pagar_descuento=0

while continuar==True:
    menu=int(input("Escoja que desea de menú: "))
    acompanamineto=int(input("Escoja que desea de acompañamiento: "))
    bebidas=int(input("Escoja que desea de bebidos: "))
    pedidos+=1
    
    if menu==1:
        total_pagar+=9
        
    elif menu==2:
        total_pagar+=4.5
        
    else:
        total_pagar+=2.5
        
    if acompanamineto==1:
        total_pagar+=1.5
        
    elif acompanamineto==2:
        total_pagar+=1.75
        
    else:
        total_pagar+=2
        
    if bebidas==1:
        total_pagar+=2
        
    elif bebidas==2:
        total_pagar+=1.5
        
    else:
        total_pagar+=1
        
    total_pagar_iva=total_pagar+(total_pagar*0.10)
        
    if 20 <= total_pagar <= 30:
        total_pagar_descuento=total_pagar_iva-(total_pagar_iva*0.05)
        
    elif total_pagar>30:
        total_pagar_descuento=total_pagar_iva-(total_pagar_iva*0.15)
        
    else:
        total_pagar_descuento=total_pagar_iva
    
    sn=str(input("Desea continuar s/n: "))
    
    if sn=="s":
        continuar=True
        
    else:
        continuar=False
        
print("El número total de pedidos es de:", pedidos)
print("El total a pagar sin IVA es de:", round(total_pagar,2))
print("El total a pagar con IVA es de:", round(total_pagar_iva,2))
print("El precio total con el descuento aplicado dependiendo del precio es de:", round(total_pagar_descuento,2))
        