#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif.

var_1=str(input("Introduce una frase: "))

if len(var_1)>11:
    print("La frase tiene más de 11 caracteres")

elif len(var_1)<11:
    print("La frase tiene menos de 11 caracteres")
    
else:
    print("La frase tiene 11 caracteres")