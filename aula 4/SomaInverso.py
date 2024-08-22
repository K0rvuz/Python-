#Faça um programa que leia 3 valores e mostre a soma de seus inversos.

n1=float(input("Escreva o primeiro número: "))
n2=float(input("Escreva o segundo número: "))
n3=float(input("Escreva o terceiro número: "))

in1=1/n1
in2=1/n2
in3=1/n3

soma= in1+in2+in3

print(f"A soma dos inversos dos três valores é {soma}")