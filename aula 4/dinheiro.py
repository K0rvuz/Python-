'''
Faça um programa que lê um valor em reais e calcule o valor equivalente em dólares. O usuário deve informar, além do valor em reais da compra, o valor da cotação do dólar.
'''


opc=input("Você deseja converter Dolar para Real ou Real para Dolar?\n\n1-Real-dolar\n\n2-Dolar-Real")

cota=float(input("Qual a cotação? "))


while opc!='1' and opc!='2':
    print("Opção inválida")

    opc=input("Você deseja converter Dolar para Real ou Real para Dolar?\n\n1-Real-dolar\n\n2-Dolar-Real")





if opc=='1':
    real=int(input("Quantos Reais desejas converter? "))
    dolar=round(real/cota,2)
    print(f"Você tem {dolar}$ dolares")

        

elif opc=='2':
    dolar=float(input("Quantos Doláres desejas converter?"))
    real= round(dolar*cota,2)
    print(f"Você tem R${real}")
    


while True:
    continuar = input("Deseja continuar? (S/N): ").upper()
    
    if continuar.upper()=='S':

        opc=input("Você deseja converter Dolar para Real ou Real para Dolar?\n\n1-Real-dolar\n\n2-Dolar-Real")



        while opc!='1' and opc!='2':
            print("Opção inválida")

            opc=input("Você deseja converter Dolar para Real ou Real para Dolar?\n\n1-Real-dolar\n\n2-Dolar-Real")





        if opc=='1':
            real=int(input("Quantos Reais desejas converter? "))
            dolar=round(real/cota,2)
            print(f"Você tem {dolar}$")
        

        elif opc=='2':
            dolar=float(input("Quantos Doláres desejas converter?"))
            real= round(dolar*cota,2)
            print(f"Você tem R${real}")
    
    
    elif continuar.upper() =="N":
        print("Obrigado por utilizar o conversor de dinheiros!")
        break

        