#For contador in string con in range:
    
var="12345 buenos días"
cont_letra=0
cont_num=0


for contador in range(0,len(var)):
        if var[contador].isnumeric():
            cont_num+=1
        if var[contador].isalpha():
            cont_letra+=1
            
print("El total de letras es:", cont_letra)
print("El total de números es:", cont_num)