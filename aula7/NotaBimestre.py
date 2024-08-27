'''

Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota1=  float(input("Digite a primeira nota: "))
while nota1<0  or nota1>10:
        nota1=  float(input("Nota invalida, digite novamente: "))
nota2=  float(input("Digite a segunda nota: "))
while nota2<0  or nota2>10:
            nota2=  float(input("Nota invalida, digite novamente: "))
nota3=  float(input("Digite a terceira nota: "))
while  nota3<0  or nota3>10:
    nota3=  float(input("Nota invalida, digite novamente: "))
nota4=  float(input("Digite a quarta nota: "))
while nota4<0  or nota4>10:
    nota4=  float(input("Nota invalida, digite novamente: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
if media<6:
        print("Você está reprovado")
else:
    print("Você está aprovado")
    print(f"Sua média é {media:.2f}")
