def soma (num1,num2):
    return num1 + num2
print(soma)

def  subtracao (num1,num2):
    return num1 - num2
print(subtracao)

def  multiplicacao (num1,num2):
    return num1 * num2
print(multiplicacao)

def divisao(num1,num2):
    return num1/num2
    
print(divisao)


num1= int(input("Escreva o número 1:"))
num2= int(input("Escreva o número 2:"))
opcao=  input("Escolha a operação: +, -, *, /")

if opcao == "+":
    print(num1, "+", num2, "=", soma(num1,num2))
    
elif opcao == "-":
    print(num1, "-", num2, "=", subtracao(num1,num2))

elif opcao == "*":
    print(num1, "*", num2, "=", multiplicacao(num1,num2))

elif opcao == "/":
    print(num1, "/", num2, "=", divisao(num1,num2))

else:
    print("Operação inválida")








