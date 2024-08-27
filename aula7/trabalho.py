'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

'''
# Pergunta quanto você ganha por hora
salario_hora = float(input("Quantos você ganha por hora? R$ "))
# Pergunta o número de horas trabalhadas no mês
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês?"))
# Calcula o total do salário no mês
salario_mensal = salario_hora * horas_trabalhadas
# Mostra o total do salário no mês
print(f"O seu salário no mês é de R${salario_mensal:.2f}")