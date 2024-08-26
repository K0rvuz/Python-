'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''

num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite outro número inteiro: "))

for i in range(num1,num2):
    print(i)


#Alteração 
'''
Altere o programa anterior para mostrar no final a soma dos números.
'''

num1= int(input("Digite um número inteiro: "))
num2= int(input("Digite outro número inteiro: "))
soma=0

for i in range(num1,num2):
    print(i)
    soma+=i
print(soma)

