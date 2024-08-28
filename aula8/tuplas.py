

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
