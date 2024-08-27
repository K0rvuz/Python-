'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

* comprar apenas latas de 18 litros;

* comprar apenas galões de 3,6 litros;

* misturar latas e galões, de forma que o desperdício de tinta seja menor.

* Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
###valor da area
area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

#########################
######bloco de calculos##
#########################
tinta_necessaria = (area / 6) + 0.1

latas_necessarias = (tinta_necessaria / 18)

galoes_necessarios = (tinta_necessaria / 3.6)

preco_lata = 80.00

preco_galo = 25.00

preco_total_latas = (latas_necessarias * preco_lata)

preco_total_galoes = (galoes_necessarios * preco_galo)

preco_total_mistura = (int(latas_necessarias) * preco_lata) #recebe um valor

preco_total_mistura = preco_total_mistura + ((galoes_necessarios -  int(galoes_necessarios)) * preco_galo) #recebe um novo valor usando o anterior como referencia

preco_total_mistura = preco_total_mistura + ((latas_necessarias -  int(latas_necessarias)) * preco_lata)
#mesma coisa do modelo anterior





#############################################################


##################
#bloco de resultado
##################
print(f"Quantidade de latas de 18 litros necessárias: {int(latas_necessarias)}")
print(f"Quantidade de galões de 3,6 litros necessários: {int(galoes_necessarios)}")
print(f"Preço total para comprar apenas latas de 18 litros: R${preco_total_latas:.2f}")
print(f"Preço total para comprar apenas galões de 3,6 litros: R${preco_total_galoes:.2f}")
print(f"Preço total para comprar latas e galões: R${preco_total_mistura:.2f}")
