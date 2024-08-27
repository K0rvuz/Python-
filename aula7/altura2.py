'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
def peso_ideal(h, sexo):
    if sexo == 'homem':
        return (72.7*h) - 58
    elif sexo == 'mulher':
        return (62.1*h) - 44.7

h = float(input('Digite a altura: '))
sexo = input('Digite o sexo biológico (homem/mulher): ')
print(f" Seu  peso ideal é: {peso_ideal(h, sexo)}Kg")  