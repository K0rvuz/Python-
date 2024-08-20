'''
Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa.
Mostrar o conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.
'''


vA=float(input("Digite a Variável A: "))
vB=float(input("Digite a Variável B: "))
vC=vA
vD=vB
print(f"A variável 'A' recebeu o valor de: {vA}\n\nA variável  'B' recebeu o valor de: {vB}\n\nA troca das variáveis ocasionou em 'A' receber {vD} e a variável  'B' receber {vC}")  



'''
Outra forma de resolver o mesmo problema:
'''
vA=float(input("Digite a Variável A: "))
vB=float(input("Digite a Variável B: "))


print(f"A variável 'A' recebeu o valor de: {vA}\n\nA variável  'B' recebeu o valor de: {vB}\n\n")


vA,vB=vB,vA

print(f"A troca das variáveis ocasionou em 'A' receber {vA} e a variável  'B' receber {vB}")