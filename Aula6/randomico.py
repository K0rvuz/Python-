'''
O programa escolhe um número aleatório (número Secreto) entre 1 e 100. O usuário tenta adivinhar o número. O programa dá dicas de "maior" ou "menor" até o usuário acertar, o programa deve contar quantas tentativas o usuário usou para acertar.
'''
import random
numero_secreto = random.randint(1, 100)
tentativas = 0
numero= int(input("Digite um número"))
while numero< numero_secreto:
    tentativas += 1
    print("maior")
    numero = int(input("Digite um número"))

while numero> numero_secreto:
        tentativas += 1
        print("menor")
        numero = int(input("Digite um número"))
        print(f"Você acertou o número secreto em {tentativas} tentativas")
        break
        
