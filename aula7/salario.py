'''
 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
* salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.
* calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
#################
#dados
#################

salario_hora = float(input("Qual é o seu salário por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês?"))
############### Salario bruto
salario_bruto = salario_hora * horas_trabalhadas
#####################

#################descontos
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
#####################

#salario liquido
salario_liquido = salario_bruto - (desconto_ir + desconto_inss +  desconto_sindicato)
###############################
######bloco  de impressão######
###############################
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"IR (11%): R${desconto_ir:.2f}")
print(f"INSS (8%): R${desconto_inss:.2f}")
print(f"Sindicato (5%): R${desconto_sindicato:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
##############################
