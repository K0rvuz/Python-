'''
Escreva um programa que transforme o valor correspondente a um intervalo temporal, expresso em horas, minutos e segundos, no valor correspondente em segundos.
'''
hora=int(input("Escreva o número de horas: "))
minuto=int(input("Escreva o número de minutos"))
segundo=int(input("Escreva os números de segundos"))

tudo=(hora*3600)+(minuto*60)+(segundo)

print(f"Valor em segundos de {hora} horas, {minuto} minutos e {segundo} segundos, é: {tudo} segundos")