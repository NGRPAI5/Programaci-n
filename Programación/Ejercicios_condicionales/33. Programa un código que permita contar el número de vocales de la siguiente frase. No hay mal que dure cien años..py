#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años.

var_1=str(input("Introduce una frase para contar el número de vocales: "))
frase_minusculas=var_1.lower()

vocal_1=frase_minusculas.count("a")
vocal_2=frase_minusculas.count("e")
vocal_3=frase_minusculas.count("i")
vocal_4=frase_minusculas.count("o")
vocal_5=frase_minusculas.count("u")

print(f"El número de a es de {vocal_1}, el número de e es de {vocal_2}, el número de i es de {vocal_3}, el número de o es de {vocal_4} y, por último, el número de u es de {vocal_5}")
