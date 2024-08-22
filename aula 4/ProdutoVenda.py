'''
Faça um programa que lê o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na tela o nome do produto e o valor total da venda.
'''

nome=input("Escreva o nome do produto: ")

quantidade=float(input("Quantos desejas comprar? "))

valor=float(input("Qual o valor do produto? "))

valor_total=valor*quantidade

desconto=input("O produto tem desconto? \n\n S-sim N-não").upper()


while True:

    if desconto.upper() =='S':
        Valor_do_desconto=float(input("Qual o valor do desconto em %? "))
        v=Valor_do_desconto/100
        print(f"Nome do produto: {nome}\nValor total:{valor_total-(valor_total*v)}")
        break


    elif desconto.upper()=='N':
        print(f"Nome do produto: {nome}\nValor total: {valor_total}")
        break



    else: 
        print("Opção inválida")
        break


while True:
    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar.upper() =="N":
        print("Obrigado por utilizar o caixa!")
        break


