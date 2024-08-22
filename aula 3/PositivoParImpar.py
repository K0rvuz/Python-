n=int(input("Digite um número: "))
if n==0:
    print(f"{n} é zero ",end='')
elif n>0:
    print(f"{n} é positivo ",end='')
else:
    print(f"{n} é negativo ",end='')

if n%2==0:
    print(f"e é par ",end='')
else:
    print(f"e é impar ",end='')