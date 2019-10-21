"""17______lista_1.py em 2018-12-08. Projeto Curso em Video.

Listas (Parte 1)

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que
permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

"""
from funcoes import cabecalho, ansi

if __name__ == '__main__':
    cabecalho('Listas (Parte 1)')

    cabecalho('Variáveis compostas', 50, '-')
    print('''\tAtribuição para variáveis vazias
    
    tupla = () ou tuple()
    lista = [] ou list()
    dicionário = {} ou dict()''')

    cabecalho('-' * 50)
    num = [2, 5, 9, 1]
    print(f'num = {num}')
    print('\t   0  1  2  3\t(índices)')
    num[2] = 3
    print(f'num[2] = 3 => {num}')
    print('\t\t\t   0  1  2  3\t(índices)')
    num.sort()
    print(f'num.sort() => {num}')
    num.sort(reverse=True)
    print(f'num.sort(reverse=True) => {num}')
    num.insert(2, 0)
    print(f'num.insert(2, 0) => {num}')
    print('\t\t\t\t\t 0  1  2  3  4\t(índices)')
    num.pop()
    print(f'num.pop() => {num}')
    print('\t\t\t  0  1  2  3\t(índices)')
    num.pop(2)
    print(f'num.pop(2) => {num}')
    print('\t\t\t   0  1  2\t(índices)')
    num.insert(2, 2)
    print(f'num.insert(2, 2) => {num}')
    print('\t\t\t\t\t 0  1  2  3\t(índices)')
    num.remove(2)
    print(f'num.remove(2) => {num}')
    print('\t\t\t\t  0  1  2\t(índices)')
    print(f'num.index(3) => {num.index(3)}')
    print('''
    if 4 in num:
        num.remove(4)
    else:
        print('Não achei o número 4.')''')
    if 4 in num:
        num.remove(4)
    else:
        print(f'{ansi("bold", "vermelho")}Não achei o número 4.{ansi()}\n')
    print(f'num => {num}')
    print('\t\t0  1  2\t(índices)')
    print(f'len(num) = {len(num)}')

    cabecalho('Looping para listas', 50, '-')
    print('''\tvalores = [5, 9, 4]
    for v in valores:
        print(f'{v}...', end='')
        ''')
    valores = [5, 9, 4]
    for v in valores:
        print(f'{v}...', end='')
    print('''
    \n\tfor k, v in enumerate(valores):
        print(f'No índice {k} encontrei o valor {v}!')
        ''')
    for k, v in enumerate(valores):
        print(f'No índice {k} encotrei o valor {v}.')

    print('''
    novos_valores = []
    for cont in range(0, 5):
        novos_valores.append(int(input('Digite um número: ')))
        ''')
    novos_valores = []
    for cont in range(0, 5):
        novos_valores.append(int(input('Digite um número: ')))

    print(f'novos_valores => {novos_valores}')

    cabecalho('Observação', 50, '-')
    print('''\ta = [2, 3, 4, 7]
    b = a
    ''')
    a = [2, 3, 4, 7]
    b = a
    print(f'Lista A: {a}')
    print(f'Lista B: {b}\n')
    b[2] = 8
    print('''\tb[2] = 8
    ''')
    print(f'Lista A: {a}')
    print(f'Lista B: {b}')
    b = a[:]
    print('''
    b = a[:]
    ''')
    print(f'Lista A: {a}')
    print(f'Lista B: {b}')
    b[2] = 4
    print('''
    b[2] = 4
    ''')
    print(f'Lista A: {a}')
    print(f'Lista B: {b}')
