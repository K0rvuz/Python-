'''
Crie um programa que compara dois números e informa qual deles é maior. O programa deve solicitar ao usuário para digitar dois números e, em seguida, imprimir uma mensagem indicando o maior número ou se os números são iguais.
'''

a= float(input("Digite o primeiro número: "))
b= float(input("Digite o segundo número: "))
if a > b:   
    print(f"{a} é  maior que {b}")

elif a < b:
    print(f"{b}  é maior que {a}")
else:
    print("Os números são iguais")

continuar=  input("Deseja continuar? (S/N): ")
while continuar.upper() != "s" or "S" and continuar.upper()  != "n" and continuar.upper() != "N":
    
    print("Opção inválida,  por favor digite S para continuar ou N para sair")
    
    continuar = input("Deseja continuar? (S/N): ")
    
    if continuar.upper() == "s" or continuar.upper() == "S":
    
        a= float(input("Digite o primeiro número: "))
    
        b= float(input("Digite o segundo número: "))
    
        if a > b:   
                print(f"{a} é  maior que {b}")

        elif a < b:
            print(f"{b}  é maior que {a}")
        else:
            print("Os números são iguais")

    elif continuar.upper() == "n" or continuar.upper() == "N":
        print("Obrigado por usar o programa!")
        break
