#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.

var_1=int(input("Inserta el número de menores de 18 años: "))
var_2=int(input("Inseta el número de mayores de 18 años o adultos: "))
precio_menores=12-(12*50/100)
precio_mayores=12-(12*10/100)
precio_total_menores=var_1*precio_menores
precio_total_mayores=var_2*precio_mayores
total=var_1*precio_menores+var_2*precio_mayores

print("El precio total de las entradas para los menores de edad introducidos anteriormente son de:",round(precio_total_menores,2))
print("El precio total de las entradas para los mayores de edad introducidos anteriormente son de:",round(precio_total_mayores,2))
print("El precio total sumando las entradas de los menores y la de los mayores son de:",round(total,2))
