vocales="aeiou"
consonantes="bcdfghjklmnpqrstvwxyz"

letra=input()
letra_2=letra.lower()

if letra.isupper():
    print("uppercase")
    
else:
    print("lowercase")
    
if letra_2 in vocales:
    print("vowel")
    
else:
    print("consonant")