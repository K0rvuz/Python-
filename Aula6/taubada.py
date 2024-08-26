# Solicite ao usuário um número e o limite da tabuada e imprima a tabuada desse número até um limite definido pelo usuário.

# Solicita ao usuário um número para a tabuada
numero = int(input("Digite um número para gerar a tabuada: "))

# Solicita ao usuário o limite da tabuada
limite = int(input("Digite o limite da tabuada: "))

# Inicializa o contador
contador = 1

# Imprime a tabuada até o limite definido usando um loop while
print(f"Tabuada do {numero} até {limite}:")
while contador <= limite:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1