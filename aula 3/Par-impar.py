'''
Escreva um programa que determine se um número é par ou ímpar. O programa deve pedir ao usuário para digitar um número inteiro e, em seguida, informar se o número é par ou ímpar.
'''


n=int(input("Digite um número: "))

if n%2==0:
    print(f"e é par ",end='')
else:
    print(f"e é impar ",end='')



'''
extensão  do programa anterior para que ele também pergunte ao usuário se ele deseja continuar ou não.
'''


n=int(input("Digite um número: "))
if n%2==0:
    print(f"{n} é par ")
else:
    print(f"{n} é impar ")

continuar = input("Deseja continuar? (S/N): ")

while continuar.upper() != "s" or "S" and continuar.upper()  != "n" and continuar.upper() != "N":
    print("Opção inválida,  por favor digite S para continuar ou N para sair")
    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() == "s" or continuar.upper() == "S":
        n=int(input("Digite um número: "))
        if n%2==0:
            print(f"{n} é par ")
        else:
                print(f"{n} é impar ")
    elif continuar.upper() == "n" or continuar.upper() == "N":
        print("Obrigado por usar o programa!")
        break

