'''
Desenvolva um programa que verifica se uma pessoa é maior de idade. O programa deve solicitar a idade do usuário e imprimir uma mensagem informando se ele é maior ou menor de 18 anos.
'''

idade=int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")



'''
outra forma de resolver o problema

'''


ano=  int(input("Em que ano você nasceu? "))
ano_atual = 2024
idade = ano_atual - ano
if idade >= 18:
    print("Você é maior de idade")

else:
        print("Você é menor de idade")

'''
------------------------------------------------
'''