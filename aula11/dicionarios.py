'''
Dicionários
Exemplos de Dicionários em Python
O que é um dicionário em Python?
Um dicionário em Python é uma coleção não ordenada de pares chave-valor. Imagine um dicionário real, onde você encontra palavras (chaves) e seus significados (valores). Em Python, as chaves devem ser únicas e imutáveis (como strings ou números), enquanto os valores podem ser de qualquer tipo de dado.
Sintaxe:

Python
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 3}
Exemplos:
Dicionário de Contatos:

Python
contatos = {'João': '123456789', 'Maria': '987654321', 'Pedro': '555555555'}
Aqui, os nomes são as chaves e os números de telefone são os valores.
Dicionário de Informações Pessoais:

Python
pessoa = {'nome': 'Ana', 'idade': 30, 'cidade': 'São Paulo', 'interesses': ['leitura', 'música', 'cozinhar']}
Neste exemplo, temos um dicionário aninhado, onde o valor da chave 'interesses' é outra lista.
Dicionário de Produtos:

Python
produtos = {'celular': 1500, 'notebook': 3000, 'tablet': 800}
As chaves são os nomes dos produtos e os valores são os preços.
Dicionário de Traduções:

Python
traducoes = {'hello': 'olá', 'goodbye': 'adeus', 'thank you': 'obrigado'}
Um dicionário simples para traduções de palavras.
Acesso aos Valores:

Python
print(contatos['João'])  # Imprime o número de telefone do João
print(pessoa['idade'])   # Imprime a idade da Ana
Modificando Valores:

Python
pessoa['idade'] = 31
print(pessoa['idade'])  # Imprime a nova idade
Adicionando Novos Pares:

Python
contatos['Ana'] = '444444444'
print(contatos)
Removendo Pares:

Python
del contatos['Pedro']
print(contatos)
Verificando se uma Chave Existe:

Python
if 'Maria' in contatos:
    print('Maria está nos contatos.')
Iterando sobre um Dicionário:
Python
for chave, valor in produtos.items():
    print(f'O produto {chave} custa R${valor}')



Por que usar dicionários?
Organização: Permitem organizar dados de forma eficiente, associando chaves a valores.
Flexibilidade: Os valores podem ser de qualquer tipo de dado, incluindo outros dicionários ou listas.
Acesso rápido: O acesso aos valores é feito diretamente pela chave, tornando a busca muito rápida.
Versatilidade: São amplamente utilizados em diversas áreas da programação, desde simples armazenamento de dados até estruturas de dados mais complexas.


Em resumo:
Os dicionários são uma estrutura de dados fundamental em Python, oferecendo uma maneira intuitiva e eficiente de armazenar e manipular dados. Sua flexibilidade e facilidade de uso os tornam uma ferramenta essencial para qualquer programador Python.
Operações Comuns em Dicionários Python
Operações comuns em dicionários Python são as ações que você realiza com frequência para manipular e acessar os dados armazenados neles. Vamos explorar as principais:
1. Acesso a Valores:
Pela chave:
Python
meu_dicionario = {'nome': 'Alice', 'idade': 30}
print(meu_dicionario['nome'])  # Imprime: Alice
Método get(): Permite definir um valor padrão caso a chave não exista:
Python
print(meu_dicionario.get('cidade', 'Não encontrada'))  # Imprime: Não encontrada
2. Adicionar Novos Pares Chave-Valor:
Atribuição direta:
Python
meu_dicionario['profissao'] = 'Programador'
3. Modificar Valores:
Atribuição:
Python
meu_dicionario['idade'] = 31
4. Remover Pares Chave-Valor:
Método pop(): Remove e retorna o valor associado à chave:
Python
valor_removido = meu_dicionario.pop('idade')
Palavra-chave del: Remove o par chave-valor:
Python
del meu_dicionario['profissao']
5. Verificar se uma Chave Existe:
Operador in:
Python
if 'nome' in meu_dicionario:
    print('A chave "nome" existe.')
6. Obter Todas as Chaves, Valores ou Ambos:
Métodos keys(), values(), items():
Python
chaves = meu_dicionario.keys()
valores = meu_dicionario.values()
pares = meu_dicionario.items()
7. Iterar sobre um Dicionário:
Loop for:
Python
for chave, valor in meu_dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')
Exemplo Completo:
Python
aluno = {'nome': 'João', 'idade': 20, 'notas': [8, 7, 9]}

# Acessando valores
print(aluno['nome'])

# Adicionando nova chave
aluno['curso'] = 'Ciência da Computação'

# Modificando valor
aluno['notas'][0] = 9

# Removendo chave
del aluno['idade']

# Iterando sobre o dicionário
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
Outras operações úteis:
Copiar um dicionário: novo_dicionario = meu_dicionario.copy()
Verificar se um dicionário está vazio: if not meu_dicionario:
Mesclar dicionários: dicionario3 = {**dicionario1, **dicionario2} (Python 3.5+)
Observações:
Chaves devem ser únicas e imutáveis: Geralmente são strings ou números.
Valores podem ser de qualquer tipo: Números, strings, listas, outros dicionários, etc.
Ordem das chaves: Não há uma ordem garantida para as chaves em um dicionário.
'''

contatos = {'João': '123456789', 'Maria': '987654321', 'Pedro': '555555555'}
print(contatos)
print(contatos['João'])

for chave in contatos:
    print(chave, contatos[chave])
# Imprime o número de telefone do João
print('\nPessoas')
pessoa = {'nome': 'Ana', 'idade': 30, 'cidade': 'São Paulo', 'interesses': ['leitura', 'música', 'cozinhar']}
for chave in pessoa:
    if chave != 'interesses':
        print(chave,pessoa[chave])
    else:
        for i in range(len(pessoa[chave])):
            print(pessoa[chave][i])

produtos = {'celular': 1499.99, 'notebook': 3000, 'tablet': 800}

print(f'Preco do Celular {produtos["celular"]}')
print(f'Preço do Notebook {produtos["notebook"]}')
print(f'Proço do Tablet {produtos["tablet"]}')

for chave in produtos:
    print(f'Preço do {chave} = R$ {produtos[chave]} ')
