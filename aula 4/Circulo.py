'''
Um círculo de raio 2 é colocando dentro de um retângulo de lados 5 e 7. Faça um programa que informe o tamanho da área do retângulo que não está sendo ocupada pelo círculo.
'''

pi=3.14
r=2
diametro=2*r
ac=pi*(r**2)
ar=5*7

a=round(ar-ac,2)

print(a)


