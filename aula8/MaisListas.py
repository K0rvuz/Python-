#LISTA 1 :)

notas=[7.0,6.0,9.8,'A']
print(notas)
for i in range (4):
    print(f'{i} => {notas[i]}')

lista_compras = ['banana','laranja','maçã']
print(lista_compras)
#for para listar os elementos da lista
for i in range(3):
    print(f'{i+1} => {lista_compras[i]}')
lista_compras.append("Bom-Bom")

print()
for i in range(4):
    print(f'{i+1} => {lista_compras[i]}')
print(lista_compras[3])
# .append("conteúdo") adiciona no final da Lista
produto=input('Digite Novo item para Lista:')
while produto:
    lista_compras.append(produto)
    produto=input('Digite Novo item para Lista:')

print(lista_compras)
for i in range(len(lista_compras)):
    print(f'{i}= {i+1} => {lista_compras[i]}')

##########################################################
#TUPLAS x LISTAS

#LISTA 2 :)

lista_compras = ['banana','laranja','maçã']
print(lista_compras)

tupla_compras = ('banana','laranja','maçã')
print(tupla_compras)

lista_compras[0]='Mamão'
print(lista_compras)

tupla_compras.append('Mamão')
print(tupla_compras)

for i in range(3):
    print(f'{i} {lista_compras[i]} {tupla_compras[i]}')

########################################################################

#LISTA 3

def listarListas():
    print("#"*30)
    for i in range(len(lista_compras)):
        print(f'{i}, {lista_compras[i]}')
    print("#"*30)

'''                  0        1        2  '''
lista_compras = ['banana','laranja','maçã']
'''                  -3       -2       -1  '''

print(lista_compras)

for i in range(3):
    print(f'{i}, {lista_compras[i]}')
print("#"*30)
for j in range(-1,-4,-1):
    print(j, lista_compras[j])
print("#"*30)
# substitui (edita) a posição
lista_compras[1]='abobora'
print(lista_compras)
# isere na posição desejada
lista_compras.insert(1,'carro')
listarListas()


lista_compras.append('carro')
listarListas()
indiceCarro=lista_compras.index('carro')
print(f'Vai excluir { indiceCarro}')

lista_compras.remove('carro')
listarListas()

indiceCarro=lista_compras.index('carro')
print(f'Vai excluir { indiceCarro}')
del lista_compras[indiceCarro]
listarListas()
'''
produto=input('Digite Novo item para Lista:')
while produto:
    lista_compras.append(produto)
    produto=input('Digite Novo item para Lista:')
'''







#######################################################################
#LISTA 4 

lista_compras = ['Banana','Laranja','maçã','morango','Mamão','pera', 'Uva', 'Abacaxi', 'Figo']
for i in range(len(lista_compras)):
    lista_compras[i]=lista_compras[i].upper()
print(lista_compras)
retira = lista_compras.pop(-1)
print(f'retira {retira}')
print(lista_compras)
retira = lista_compras.pop(-4)
print(f'retira {retira}')
print(lista_compras)
retira = lista_compras.pop(2)
print(f'retira {retira}')
print(lista_compras)
lista_compras.sort()
print(lista_compras)

for i in range(len(lista_compras)):
    lista_compras[i]=lista_compras[i].upper()

#################################################

#LISTA 5 :)

# CONCATENANDO LISTAS (UNIÃO de conjuntos )
#
lista_frutas = ['Banana','Laranja','Maçã']
lista_cereais = ['Arroz', 'Feijão','Milho', 'Ervilha']
print(lista_frutas)
print(lista_cereais)
lista_compras= lista_frutas + lista_cereais
print(lista_compras)
# Max e Min
maior = max(lista_compras)
menor = min(lista_compras)
print(f'Maior {maior} Menor {menor}')
lista_compras.sort()
print(lista_compras)
 ########################################################

#LISTA 6 :)

lista=[('Banana', 3),('Abacaxi',1),('Vitela',3)]
print (lista)
produtos=['Banana', 'Abacaxi', 'Vitela']
qtds=[3,4,3]
precos=[4.5,9.9, 54.8]
total = 0
produtos.append("Bom-bom")
qtds.append(1)
precos.append(34.9)



for i in range(len(produtos)):
    totItem= precos[i] * qtds[i]
    total+= totItem
    print(f'{produtos[i] } {qtds[i]} {precos[i]} = {totItem} ')
print(f'Total = {total}')

##############################################
#Lista 7 :)

''' Faça um programa que recebe um número
não determinado  de prods, quantidades
de venda e seus respectivos preços,
adicione em três listas prods, precos, qtds
e calcule o total da venda

'''
# Criar as listas vazias
precos=[]
qtds=[]
prods=[]
continua = 'S'
while continua.upper() == 'S':
    while True:
        try:
            produto = input("Digite um Produto:")
            quant = int(input(f"Digite quantidade de {produto}:"))
            preco= float(input(f"Digite Preço de {produto}:"))
            prods.append(produto)
            qtds.append(quant)
            precos.append(preco)
            break
        except:
            print("ALGO deu errado :-(")
    continua=input("Continua S/N")
else:
    print("Encerrou Entrada")


total=0
for i in range(len(prods)):
    totItem= precos[i] * qtds[i]
    total+= totItem
    print(f'{prods[i] } {qtds[i]} {precos[i]} = {totItem} ')
print(f'Total = {total}')



