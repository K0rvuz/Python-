'''
1. Faça uma lista com o nome de 5 pessoas
'''

Lista_Nomes= ['Lucas', 'Maria', 'Juliana', 'Julio',  'Pedro']
print(Lista_Nomes)

'''
2. Mostre o tamanho da lista, liste a lista um elemento em cada linha e liste somente o Terceiro elemento da lista

'''
print(len(Lista_Nomes))
for i in range(len(Lista_Nomes)):
    print(Lista_Nomes[i])
    print(Lista_Nomes[2])

'''
3. A partir da seguinte lista Alunos=['Adriano', 'Arthur','Eduarda','Dan','Alexandro','Jamile', Rafael'] , roque o sexto elemento da lista por 'Nícolas'
mostre a lista modificada
'''
Alunos=['Adriano', 'Arthur','Eduarda','Dan','Alexandro','Jamile','Rafael']

Alunos[5] = 'Nícolas'

print(Alunos)

'''
4. insira no Final da Lista 'Vitor'
'''
Alunos.append('Vitor')
print(Alunos)

'''
5.Insira na 5 Posição 'Álvaro'
'''
Alunos.insert(4, 'Álvaro')
print(Alunos)

'''
6. Adicione na terceira posição o nome 'Eliana' e na sexta posição 'Carlos'
'''
Alunos.insert(2, 'Eliana')
Alunos.insert(5, 'Carlos')
print(Alunos)

'''
7. Liste todos elementos de lista em ordem inversa
'''
print(Alunos[::-1])

'''
8. Crie uma lista de compras com um número ideterminado de ítens a serem comprados encerrar quando ítem = vazio
'''
compras = []
while True:
    item = input('Digite o item a ser comprado: ')
    if item == '':
        break
    compras.append(item)
    print(compras)

'''
9-A partir da lista linguagens=['Java', 'Python', 'C', 'C++', 'PHP'] verifique se a linguagem Pytho está na lista e qual sua posição de índice
'''
linguagens = ['Java', 'Python', 'C', 'C++', 'PHP']
print('Linguagem Python está na lista? ', 'Python' in linguagens)
print('Posição da linguagem Python na lista: ', linguagens.index('Python'))
print('Posição da linguagem Python na lista: ', linguagens.index('Python')+1)

'''
10 A partir da lista Linguagens, verifique se a Linguagem 'Basic' está na lista e qual sua posição caso esteja. Trate o erro se ocorrer e mostre uma menssagem. 
'''
while True:
    try:
        print('Linguagem Basic está na lista? ', 'Basic' in linguagens)
        print('Posição da linguagem Basic na lista: ', linguagens.index('Basic')+1)
    except:
            print('Linguagem Basic não está na lista')
            break


'''
11 Crie uma lista com nomes de alunos e outra com nome de professores, concatene as duas listas na lista pessoas. 

'''
alunos = ['João', 'Maria', 'Pedro']
professores = ['Eduardo', 'Ana', 'Carlos']
pessoas = alunos + professores
print(pessoas)

'''
12 crie uma lista de números com uma quandidade indeterminada (use While True:)
     mostre o maior número, o menor, a média dos números. 
'''
numeros = []
while True:
    try:
        num = float(input('Digite um número: '))
        numeros.append(num)
    except:
        print('Número inválido')
        break
print('Maior número: ', max(numeros))
print('Menor número: ', min(numeros))
print('Média dos números: ', sum(numeros)/len(numeros))

'''
14. Mostre a posição do Maior e a posição do Menor número

'''
print('Posição do Maior número: ', numeros.index(max(numeros)))
print('Posição do Menor número: ', numeros.index(min(numeros)))

'''
15. mostre a soma dos números da Lista
'''
print('Soma dos números: ', sum(numeros))
