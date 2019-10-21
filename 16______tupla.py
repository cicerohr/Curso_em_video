"""16______tupla.py em 2018-12-07. Projeto Curso em Video.

Tupla

Nessa aula, vamos aprender o que é TUPLA e como utilizar tupla em Python. A tupla é uma variável composta e
imutável que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Tupla')

    cabecalho('Variáveis compostas', 50, '-')
    print('''\tAtribuição para variáveis vazias
    
    tupla = () ou tuple()
    lista = [] ou list()
    dicionário = {} ou dict()''')

    cabecalho('Tupla', 50, '-')
    print('Obs.: tupla é imutáveis\n')
    lanche = ('Hamburger', 'Cachorro-quente', 'Pizza', 'Pudim')
    print(f'lanche = {lanche}')
    print('\t\t\t   0\t\t\t\t1\t\t\t 2\t\t  3\t\t(índices)')
    print(f'len(lanche) = {len(lanche)}')
    print(f'lanche[1] => {lanche[1]}')
    print(f'lanche[3] => {lanche[3]}')
    print(f'lanche[-2] => {lanche[-2]}')
    print(f'lanche[-4] => {lanche[-4]}')
    print(f'lanche[-1] => {lanche[-1]}')
    print(f'lanche[1:3] => {lanche[1:3]}')
    print(f'lanche[2:] => {lanche[2:]}')
    print(f'lanche[:2] => {lanche[:2]}')
    print(f'lanche[-2:] => {lanche[-2:]}')
    print(f'lanche[:-2] => {lanche[:-2]}')
    print(f'lanche[::-1] => {lanche[::-1]}\tObs.: inverte a sequencia')

    cabecalho('Laços para mostrar o conteúdo da tupla', 50, '-')
    print('''\tfor comida in lanche:
        print(f'Eu comi {comida}.')
        ''')
    for comida in lanche:
        print(f'Eu comi {comida}.')

    print('''
    for c in range(0, len(lanche)):
        print(f'Eu comi {lanche[c]} no índice {c}.')
        ''')
    for c in range(0, len(lanche)):
        print(f'Eu comi {lanche[c]} no índice {c}.')

    print('''
    for i, comida in enumerate(lanche):
        print(f'Eu comi {comida} no índice {i}.')
        ''')
    for i, comida in enumerate(lanche):
        print(f'Eu comi {comida} no índice {i}.')

    cabecalho('Mostrar a tupla em ordem alfabética', 50, '-')
    print('''\tprint(sorted(lanche))
    ''')
    print('Obs.: gera uma lista para ordenar a tupla')
    print(f'sorted(lanche) => {sorted(lanche)}')
    print(f'lanche = {lanche}')

    cabecalho('Concatenação de tupla', 50, '-')
    print('''\ta = (2, 5, 4)
    b = (5, 8, 1, 2)
    c = a + b
    print(c)
    ''')
    a = (2, 5, 4)
    b = (5, 8, 1, 2)
    c = a + b
    print(f'c = {c}')

    cabecalho('Métodos', 50, '-')
    print(f'c = {c}')
    print('\t 0  1  2  3  4  5  6\t(índices)')
    print(f'len(c) = {len(c)}')
    print(f'c.count(5) => {c.count(5)} (conta quantas vezes aparece o número 5)')
    print(f'c.count(9) => {c.count(9)} (conta quantas vezes aparece o número 9)')
    print(f'c.index(8) => {c.index(8)} (qual o índice do número 8)')
    print(f'c.index(5) => {c.index(5)} (qual o índice do número 5)')
    print(f'c.index(5, 2) => {c.index(5, 2)} (qual o índice do número 5 a partir do índice 2)')
