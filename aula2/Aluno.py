'''
Faça um programa que recebe o nome de um aluno e suas três notas
e calcula a media do aluno, no final  mostra seu nome, suas notas e sua média.

''' 
nome= input("Digite seu nome:")
matricula=int(input("Digite sua matricula: "))


nota1=float(input("Digite sua primeira nota: "))
while nota1>10 or nota1<0:
    do:  print("Nota invalida, tente novamente")
    nota1=float(input("Digite sua primeira nota: "))

nota2=float(input("Digite sua segunda nota: "))

while nota2>10 or nota2<0:
        print("Nota invalida, tente novamente")
        nota2=float(input("Digite sua segunda nota: "))



nota3=float(input("Digite sua terceira nota: "))


while nota3>10 or nota3<0:
        print("Nota invalida, tente novamente")
        nota3=float(input("Digite sua terceira nota: "))

media=(nota1+nota2+nota3)/3



if media>=7:
    print(f"Nome: {nome}\nMatricula: {matricula}\nMédia: {media}\n\nAprovado")
elif media<7 and media>=4:
    print(f"Nome: {nome}\nMatricula: {matricula}\nMédia: {media}\n\nRecuperação")
else:
    print(f"Nome: {nome}\nMatricula: {matricula}\nMédia: {media}\n\nReprovado")

