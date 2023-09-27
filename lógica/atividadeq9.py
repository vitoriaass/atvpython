altura = float(input("digite a altura"))
sexo = input("digite M ou F")
if sexo== "M":
    peso_ideal =(72.7 * altura) - 58
    print ("o peso ideal do homem com altura metros de altura e peso_ideal Kg")
elif sexo =="F":
    peso_ideal = (62.7 * altura) - 44.7
    print("o peso ideal para uma mulher com altura metros de altura e pesp_ideal Kg")