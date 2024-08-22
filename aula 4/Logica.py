'''
Escreva uma expressão lógica que seja verdadeira no caso do valor lido do teclado estar compreendido entre 10 e 50. O programa deve imprimir na tela o resultado da expressão lógica (True ou False).
'''

valor=float(input("Escreva um número"))

if valor>=10 and valor<=50:
    print("True")
else:
    print("False")