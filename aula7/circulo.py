'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
# Importando a biblioteca math para usar a função pi
import math

raio = float(input('Digite o raio do círculo: '))
area = math.pi * (raio ** 2)
print(f'A área do círculo é {area:.2f}')  
