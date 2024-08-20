num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
num3=float(input("Digite o terceiro número: "))
num4=float(input("Digite o quarto número: "))
num5=float(input("Digite o quinto número: "))

def  media(num1,num2,num3,num4,num5):
    return  (num1+num2+num3+num4+num5)/5
def soma(num1,num2,num3,num4,num5):
    return (num1+num2+num3+num4+num5)


print(f"A soma desses 5 números é:\n{soma(num1,num2,num3,num4,num5)}\n\ne a média é:\n{media(num1,num2,num3,num4,num5)}")


