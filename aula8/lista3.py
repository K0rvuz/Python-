
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



