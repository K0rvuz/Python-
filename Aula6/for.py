# Exemplos de FOR


'''
quando o passo é POSITIVO enquanto <
for começando em 0 enquanto <5 de 1 em 1 (passo)
'''
for i in range (5):
    print(i)
'''
for começando em 0 enquanto <5 de 1 em 1 (passo)
'''
for i in range (0,5,1):
    print(i)
print("###############")
'''
passo for negativo enquanto >
for começando em -1 enquanto >-5 de -1 em -1 (passo)
'''
for i in range(0, -5,-1):
    print(i)
'''
passo for negativo enquanto >
for começando em -1 enquanto >10 de -2 em -2 (passo)
'''
for i in range(30, 10,-2):
    print(i)

'''
começa 10
passo -2 (negativo)
enquanto > 30 (NÃO EXECUTA O FOR)
'''
for i in range(10,30,-2):
    print(i)
print("Tô aqui")
'''
começa 55
passo 3 (POSITIVO)
enquanto < 10 (NÃO EXECUTA O FOR)
'''
for i in range (55,10,3):
    print(i)
print("Tô fora")