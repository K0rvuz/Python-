'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

soma=0 # variável acumuladora
for i in range(5):
    num=float(input('Digite um número:'))
    soma += num

print(f'Soma = {soma}')
print(f'media= {soma/5}')