'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
# Iniciando o programa
print("Números ímpares entre 1 e 50: ")
        # Utilizando um loop para imprimir os números ímpares
for i in range(1, 51): #Mostra  todos os números de 1 a 50

    if i % 2 != 0:  #verifica  se o número é ímpar
        print(i)    #imprime o número

print("Fim do programa")  #deve ficar fora do for para não repetir junto com a estrutura
'''
o % 2 diferente de 0 faz com que todos os número passem por uma "peneira". Com isso, os números que são %2=0 são eliminados da contagem por serem pares. 

'''