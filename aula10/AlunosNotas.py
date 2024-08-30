alunos = []
notas = []

while True:
    print('''
    1. Incluir nas listas
    2. Listar as listas
    3. Buscar aluno com maior nota
    4. Excluir um aluno e sua nota
    5. Calcular média da turma
    6. Fim
    ''')

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Por favor, escolha um número.")
        continue

    if opcao == 1:
        try:
            nome = input('Nome do aluno: ')
            nota = float(input(f'Nota de {nome}: '))
            while  nota < 0 or nota > 10:
                print('Nota inválida. Por favor, insira uma nota entre 0 e 10.')
                nota= float(input(f'Nota de {nome} '))
                continue
            alunos.append(nome)
            notas.append(nota)
            print('Aluno incluído com sucesso.')
        except ValueError:
            print('Nota inválida. Tente novamente.')

    elif opcao == 2:
        if alunos and notas:
            print('Alunos: ', alunos)
            print('Notas: ', notas)
        else:
            print('Lista vazia.')

    elif opcao == 3:
        if notas:
            maior_nota = max(notas)
            aluno_maior_nota = alunos[notas.index(maior_nota)]
            print(f'Aluno com maior nota: {aluno_maior_nota} (Nota: {maior_nota})')
        else:
            print('Lista de notas vazia.')

    elif opcao == 4:
        nome = input('Nome do aluno a ser excluído: ')
        if nome in alunos:
            index = alunos.index(nome)
            alunos.pop(index)
            notas.pop(index)
            print(f'Aluno {nome} excluído com sucesso.')
        else:
            print('Aluno não encontrado.')

    elif opcao == 5:
        if notas:
            media = sum(notas) / len(notas)
            print(f'Média da turma: {media:.2f}')
        else:
            print('Lista de notas vazia.')

    elif opcao == 6:
        print("Fim do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha um número entre 1 e 6.")