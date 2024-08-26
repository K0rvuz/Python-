#1 Solicite ao usuário um número inteiro positivo e faça uma contagem regressiva até 0, imprimindo cada número.


i = int(input("Digite um número: "))#pega o numero
while i>=0: #enquanto o número for maior igual a zero, faz o código
    print(i) #mostra o número
    i-=1 #faz com que o número entre em contagem regressiva usando -=
    if i == -1: #se o número for igual a -1, quebra mostrando a mensagem final
        break
print("Saiu do while!")