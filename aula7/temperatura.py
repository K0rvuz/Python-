'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F-32) / 9).
'''
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"A temperatura de {fahrenheit} graus Fahrenheit é igual a {celsius} graus Celsius.") 
