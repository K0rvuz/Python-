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
