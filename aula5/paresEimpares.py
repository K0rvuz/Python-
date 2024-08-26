'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''

def mostraTot(): #definição de uma função
    print(f'Quantidade de Impares={impares} total = {somaImpar}')
    print(f'Quantidade de pares={pares} total {somaPar}')

pares=0 # variáveis contadoras
impares=0 # variáveis contadoras
somaPar=0 # varíaveis acumuladoras
somaImpar=0  # varíaveis acumuladoras
for i in range (10):
    num=int(input(str(i)+") Digite um número"))
    if num % 2 == 0:
        pares+=1
        somaPar+=num
        #mostraTot()  chamada da função

    else:
        impares+=1
        somaImpar+=num
        #mostraTot()

mostraTot() # chamada da função
