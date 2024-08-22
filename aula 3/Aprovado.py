'''
Desenvolva um programa que avalia a nota de um aluno e informa se ele foi aprovado, está de recuperação ou foi reprovado. Considere que a nota mínima para aprovação é 7, para recuperação é 5 e para reprovação é abaixo de 5. O programa deve solicitar ao usuário para digitar a nota do aluno.
'''

nome= input("Digite o nome do aluno: ")

nota1=float(input("Coloque a primeira nota: "))

while nota1>10 or nota1<0 :
    print("Nota invalida, tente novamente")
    nota1=float(input("Coloque a primeira nota: "))


nota2=float(input("Coloque a segunda nota: "))

while  nota2>10 or nota2<0 :
    print("Nota invalida, tente novamente")
    nota2=float(input("Coloque a segunda nota: "))


nota3=float(input("Coloque a terceira nota: "))
while  nota3>10 or nota3<0 :
    print("Nota invalida, tente novamente")
    nota3=float(input("Coloque a terceira nota: "))


media=(nota1+nota2+nota3)/3


if media>=7:
    print(f"{nome} foi aprovado com média {media}.")


elif media==5:
    print(f"{nome} está de recuperação com média {media}.")


elif  media<5:
    print(f"{nome} foi reprovado com média {media}.")



