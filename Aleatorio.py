import random



def fn_soma():
    num1= random.randint(1,1000)
    num2= random.randint(1,1000)
    num3=int(input(f"Digite a soma de: {num1} + {num2} "))

    if num3 == num1+num2:
        print("Parabéns")

    while  num3 != num1+num2:
        print("Burro demais, que isso!")
        num3=int(input(f"tente novamente a soma de: {num1} + {num2} "))
        if num3 == num1+num2:
            print ("Parabéns")












def fn_adv():
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


def fn_consiste_num():
    ini = 1; fim = 0
    while ini > fim:
        ini = int(input("Início do intervalo:"))
        fim = int(input("fim do intervalo:"))
        if ini > fim: print("ERRO - ini>fim")
    return ini, fim

# fn_def_aleatorio(ini,fim): exibe um número aleatório no intervalo
# ini: inicio do intervalo
# fim: final do intervalo
# exemplo:
# entrada: ini=10; fim=20
# saída: Número aleatorio entre 10 e 20: 15

def fn_def_aleatorio(ini,fim):
    print("Número aleatorio entre "+str(ini)+" e "+str(fim)+": "+str(random.randint(ini,fim)))

# fn_lista_aleatorios(qtd,ini,fim): exibe uma lista de numeros aleatorios no intervalo
# ini: inicio do intervalo
# fim: final do intervalo
# qtd: quantidade de números aleatorios na lista gerada
# exemplo:
# entrada: qtd=5; ini=10; fim=20
# lista de saída:
# 01 -> 15
# 02 -> 17
# 03 -> 10
# 04 -> 20
# 05 -> 12
def fn_lista_aleatorios(qtd,ini,fim):
    for ct_int in range(qtd):
        print(f"{ct_int+1:02d}"+" -> "+str(random.randint(ini,fim)))
        break




