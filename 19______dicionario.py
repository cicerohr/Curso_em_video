"""19______dicionario.py em 2018-12-09. Projeto Curso em Video.

Dicionário

Nessa aula, vamos aprender o que é DICIONÁRIO e como utilizar dicionário em Python. Os dicionários são variáveis
compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

"""
from funcoes import cabecalho, ansi

if __name__ == '__main__':
    cabecalho('Dicionário')

    cabecalho('Variáveis compostas', 50, '-')
    print('''\tAtribuição para variáveis vazias
    
    tupla = () ou tuple()
    lista = [] ou list()
    dicionário = {} ou dict()
    ''')

    cabecalho('Composição do dicionário', 50, '-')
    print(f"\t\t\t\t\t\t\t{ansi('bold', 'underline', 'cyan')} items {ansi()}")
    print(f'\t\t\t{ansi("cyan")} {"_ " * 19}{ansi()}')
    print(f"\t\t\t{ansi('bold', 'cyan')}|{ansi()}{ansi('bold', 'amarelo')}'Star Wars'\t1977\t'George Lucas'{ansi()}"
          f"{ansi('bold', 'cyan')}|{ansi()}\t{ansi('bold', 'amarelo')} values{ansi()}")
    print(f'\t\t\t{ansi("bold", "cyan")}|{ansi()}{ansi("vermelho")}\ttítulo\t\tano\t\t\tdiretor{ansi()}'
          f'\t{ansi("bold", "cyan")}  |{ansi()}\t{ansi("bold", "vermelho")}  keys{ansi()}')
    print(f'\t\t\t{ansi("cyan")} {"¯ " * 19}{ansi()}')
    print('''\tfilme = {'título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
    for keys, values in filme.items():
        print(f'O {keys} é {values}.')
        ''')
    filme = {'título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
    for k, v in filme.items():
        print(f'O {ansi("vermelho")}{k}{ansi()} é {ansi("amarelo")}{v}{ansi()}.')

    cabecalho('Utilização dos dicionários', 50, '-')
    pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
    print(f'pessoas = {pessoas}')
    print(f'pessoas["nome"] => {pessoas["nome"]}')
    print(f'pessoas["idade"] => {pessoas["idade"]}')
    print(f'pessoas.keys() => {pessoas.keys()}')
    print(f'pessoas.values() => {pessoas.values()}')
    print(f'pessoas.items() => {pessoas.items()}')
    print('''
    for k in pessoas.keys():
        print(k)''')
    for k in pessoas.keys():
        print(k)
    print('''
    for v in pessoas.values():
        print(v)''')
    for v in pessoas.values():
        print(v)

    print('''
    for i in pessoas.items():
        print(i)''')
    for i in pessoas.items():
        print(i)
    print('''
    for k, v in pessoas.items():
        print(f'{k} = {v}')''')
    for k, v in pessoas.items():
        print(f'{k} = {v}')
    print('''
    pessoas['nome'] = 'Leandro'
    print(pessoas)''')
    pessoas['nome'] = 'Leandro'
    print(pessoas)
    print('''
    pessoas['peso'] = 90.2
    print(pessoas)''')
    pessoas['peso'] = 90.2
    print(pessoas)
    print('''
    del pessoas['sexo']
    print(pessoas)''')
    del pessoas['sexo']
    print(pessoas)
    print(' Ordenando Dicionários '.center(50, '-'))
    print('''
    jogadores = dict(jogador_1=3,
                     jogador_2=4,
                     jogador_3=1,
                     jogador_4=2)
    c = 0
    print(jogadores, '\\n')
    for k in sorted(jogadores, key=jogadores.get, reverse=True):
        c += 1
        print(f'{c}° lugar: {k} com {jogadores[k]}.')
    ''')
    jogadores = dict(jogador_1=3,
                     jogador_2=4,
                     jogador_3=1,
                     jogador_4=2)
    c = 0
    print(jogadores, '\n')
    for k in sorted(jogadores, key=jogadores.get, reverse=True):
        c += 1
        print(f'{c}° lugar: {k} com {jogadores[k]}.')
    print('\n', '-' * 50)
    print('''
    brasil = []
    estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
    estado2 = {'uf': 'SãoPaulo', 'sigla': 'SP'}
    brasil.append(estado1)
    brasil.append(estado2)
    ''')
    brasil = []
    estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
    estado2 = {'uf': 'SãoPaulo', 'sigla': 'SP'}
    brasil.append(estado1)
    brasil.append(estado2)
    print(f'brasil[0] => {brasil[0]}')
    print(f'brasil[1] => {brasil[1]}')
    print(f'brasil => {brasil}')
    print(f"brasil[0]['uf'] => {brasil[0]['uf']}")
    print(f"brasil[1]['sigla'] => {brasil[1]['sigla']}")
    print('''
    brasil = list()
    estado = dict()
    for c in range(0, 3):
        estado['uf'] = str(input('Unidade Federativa: '))
        estado['sigla'] = str(input('Sigla do Estado: '))
        brasil.append(estado.copy())  # método para fazer cópias
        ''')
    brasil = list()
    estado = dict()
    for c in range(0, 3):
        estado['uf'] = str(input('Unidade Federativa: ').strip().title())
        estado['sigla'] = str(input('Sigla do Estado: ').strip().upper())
        brasil.append(estado.copy())  # método para fazer cópias
    print(f'brasil => {brasil}')
    print('''
    for e in brasil:    # looping para ler a lista
        for k, v in e.items():  # looping para ler os dicionários
            print(f'O campo {k} tem valor {v}.')
            ''')
    print(brasil)
    lista = dicionario = 0
    print('\n\t\t\t\t\t\t\t\t\tlista\t\tdicionários\t(looping)')
    for e in brasil:  # looping para ler a lista
        for k, v in e.items():  # looping para ler os dicionários
            print(f'O campo {k} tem valor {v}.\t\t\t  {lista}\t\t\t\t{dicionario}')
            dicionario += 1
        dicionario = 0
        lista += 1
