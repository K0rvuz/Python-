'''
DESAFIO TEMPERATURAS

Enunciados para Conversão de Temperaturas
Enunciado 1: Conversão de Celsius para Fahrenheit

Crie um programa que converta uma temperatura em graus Celsius para Fahrenheit.

Entrada da temperatura em Celsius e calcula Fahrenheit.




Fórmula: Fahrenheit = (Celsius * 9/5) + 32
'''

n=  float(input("Digite a temperatura em Celsius: "))

f = (n * 9/5) + 32
print(f"{n} graus Celsius é igual a {f} graus Fahrenheit")  #


# 1.1




''' Enunciado 2: Conversão de Fahrenheit para Celsius
Crie um programa que converta uma temperatura em grausFahrenheit para Celsius.
Entrada da temperatura em Fahrenheit e calcula Celsius.
Fórmula: Celsius = (Fahrenheit - 32) * 5/9
Exemplo: 100 graus Fahrenheit é igual a 37,78 graus Celsius.
'''

f = float(input("Digite a temperatura em Fahrenheit: "))
c = (f - 32) * 5/9
print(f"{f} graus Fahrenheit é igual a {c} graus Celsius")  #
# 1.2


'''
Conversor Bidirecional de Temperaturas

Crie um programa que permita ao usuário escolher entre converter Celsius para Fahrenheit ou vice-versa. O programa deve solicitar a temperatura e a unidade de medida desejada, e exibir o resultado da conversão.

'''

n= input("Qual operação desejas realizar?  \n 1 - Celsius para Fahrenheit \n 2 - Fahrenheit para Celsius \n")

while n != "1" and n  != "2":
    print("Opção inválida,  tente novamente")
    n= input("Qual operação desejas realizar?  \n 1 - Celsius para Fahrenheit \n 2 - Fahrenheit para Celsius \n")





if n == "1":
    n =  float(input("Digite a temperatura em Celsius: "))
    f = (n * 9/5) + 32
    print(f"{n} graus Celsius é igual a {f} graus Fahrenheit")

elif n == "2":
        f = float(input("Digite a temperatura em Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f} graus Fahrenheit é igual a {c} graus Celsius") 







while True:
    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar.upper() =="N":
        print("Obrigado por utilizar o conversor de temperatura!")
        break
        

   
    n= input("Qual operação desejas realizar?  \n 1 - Celsius para Fahrenheit \n 2 - Fahrenheit para Celsius \n")
    while n.upper() != "1" and n.upper()  != "2":
        print("Opção inválida,  tente novamente")
        n= input("Qual operação desejas realizar?  \n 1 - Celsius para Fahrenheit \n 2 - Fahrenheit para Celsius \n")
    
                
        if n == "1":
            n =  float(input("Digite a temperatura em Celsius: "))
            f = (n * 9/5) + 32
            print(f"{n} graus Celsius é igual a {f} graus Fahrenheit")
            break



        elif n == "2":
            f = float(input("Digite a temperatura em Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f} graus Fahrenheit é igual a {c} graus Celsius")
            break

'''
Crie um programa que converta entre Celsius, Fahrenheit e Kelvin.
Pesquise sobre outras escalas de temperatura e implemente a conversão entre elas.
'''


n1= input("Escolha a temperatura que desejas: \n\n  1 - Celsius \n 2 - Fahrenheit \n 3 - Kelvin \n")

n2=  input("Escolha a temperatura que desejas converter: \n\n  1 - Celsius  \n 2 - Fahrenheit \n 3 - Kelvin \n")




#Celsius

if n1=='1':
    c = float(input("Digite a temperatura em Celsius: "))
#Celsius para Celsius    
    if  n2=='1':
        print(f"{c} graus Celsius é igual a {c} graus Celsius")
 
#Celsius para  Fahrenheit    
    elif n2=='2':
        f = (c * 9/5) + 32
        print(f"{c} graus Celsius é igual a {f} graus Fahrenheit")
#Celsius para  Kelvin
    elif n2=='3':
        k = c + 273.15
        print(f"{c} graus Celsius é igual a {k} graus Kelvin")



#Fahrenheit 
elif  n1=='2':
    
    f = float(input("Digite a temperatura em Fahrenheit: "))
    #Fahrenheit para Celsius
    if n2=='1':
        c = (f - 32) * 5/9
        print(f"{f} graus Fahrenheit é igual a {c} graus Celsius")
        #Fahrenheit para Fahrenheit
    elif n2=='2':
        print(f"{f} graus Fahrenheit é igual a {f} graus Fahrenheit")
            #Fahrenheit para Kelvin
    elif n2=='3':
        k = (f - 32) * 5/9 + 273.15
        print(f"{f} graus Fahrenheit é igual a {k} graus Kelvin")

#Kelvin
elif n1=='3':
    k = float(input("Digite a temperatura em Kelvin: "))
    #Kelvin para Celsius
    if n2=='1':
        c = k - 273.15
        print(f"{k} graus Kelvin é igual a {c} graus Celsius")
    #Kelvin para Fahrenheit
    elif n2=='2':
        f = (k - 273.15) * 9/5 + 32
        print(f"{k} graus Kelvin é igual a {f} graus Fahrenheit")
    #Kelvin para Kelvin
    elif n2=='3':
        print(f"{k} graus Kelvin é igual a {k} graus Kelvin")



