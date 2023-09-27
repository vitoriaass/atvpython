numero_indentificaçao=int(input("digite um numero"))
n1= float(input("digite um numero"))
n2= float(input("digite um numero"))
n3= float(input("digite um numero"))
media_exe= float(input("digite um numero"))
media_aprov=(n1+n2*2+n3*3+media_exe)/7
if media_aprov >=90:
    conceito="a"
    print (conceito)
elif media_aprov>= 75:
    conceito= "b"
    print (conceito)
elif media_aprov>=60:
    conceito="c"
    print (conceito)
elif media_aprov>=40:
    conceito="d"
    print (conceito)
else:
    conceito="e"
if conceito==("a or b or c"):
    print ("aprovado")
else:
    print ("reprovado")