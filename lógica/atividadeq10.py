peso = float(input("digite o peso"))
altura = float(input("digite o altura"))
imc = (altura**2)/peso
if imc < 18.5:
    print("desnutrido")
elif 18.5 <imc <25:
    print("normal")
elif 25<imc<30:
    print("acima do peso")
else:
    print("obeso")
    
