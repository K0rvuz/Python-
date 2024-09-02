def incluir_aluno(alunos, alturas, pesos):
    nome = input("Digite o nome do aluno: ")
    altura = float(input("Digite a altura do aluno (em metros): "))
    peso = float(input("Digite o peso do aluno (em kg): "))
    alunos.append(nome)
    alturas.append(altura)
    pesos.append(peso)

def listar_listas(alunos, alturas, pesos):
    print("\nLista de Alunos, Alturas e Pesos:")
    for i in range(len(alunos)):
        print(f"Aluno: {alunos[i]}, Altura: {alturas[i]}m, Peso: {pesos[i]}kg")

def buscar_maior_peso(alunos, pesos):
    if not alunos:
        print("A lista de alunos está vazia.")
        return
    index_max_peso = pesos.index(max(pesos))
    print(f"\nAluno com maior peso é {alunos[index_max_peso]} com {pesos[index_max_peso]}kg.")

def buscar_maior_altura(alunos, alturas):
    if not alunos:
        print("A lista de alunos está vazia.")
        return
    index_max_altura = alturas.index(max(alturas))
    print(f"\nAluno com maior altura é {alunos[index_max_altura]} com {alturas[index_max_altura]}m.")

def excluir_aluno(alunos, alturas, pesos):
    nome = input("Digite o nome do aluno a ser excluído: ")
    if nome in alunos:
        index = alunos.index(nome)
        alunos.pop(index)
        alturas.pop(index)
        pesos.pop(index)
        print(f"Aluno {nome} excluído com sucesso.")
    else:
        print(f"Aluno {nome} não encontrado.")

def calcular_media(alturas, pesos):
    if not alturas or not pesos:
        print("As listas estão vazias.")
        return
    media_altura = sum(alturas) / len(alturas)
    media_peso = sum(pesos) / len(pesos)
    print(f"\nMédia de altura: {media_altura}m")
    print(f"Média de peso: {media_peso}kg")

def main():
    alunos = []
    alturas = []
    pesos = []

    while True:
        print("\nMenu:")
        print("1. Incluir aluno")
        print("2. Listar alunos")
        print("3. Buscar aluno com maior peso")
        print("4. Buscar aluno com maior altura")
        print("5. Excluir aluno")
        print("6. Calcular média de altura e peso")
        print("7. Fim")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            incluir_aluno(alunos, alturas, pesos)
        elif opcao == '2':
            listar_listas(alunos, alturas, pesos)
        elif opcao == '3':
            buscar_maior_peso(alunos, pesos)
        elif opcao == '4':
            buscar_maior_altura(alunos, alturas)
        elif opcao == '5':
            excluir_aluno(alunos, alturas, pesos)
        elif opcao == '6':
            calcular_media(alturas, pesos)
        elif opcao == '7':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
