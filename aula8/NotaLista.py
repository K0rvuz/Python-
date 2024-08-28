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
