"""18______lista_2.py em 2018-12-08. Projeto Curso em Video.

Listas (Parte 2)

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que
permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Listas (Parte 2)')

    cabecalho('Variáveis compostas', 50, '-')
    print('''\tAtribuição para variáveis vazias
    
    tupla = () ou tuple()
    lista = [] ou list()
    dicionário = {} ou dict()
    ''')

    cabecalho('-'*50)
    print('''\tteste = list()
    teste.append('Gustavo')
    teste.append(40)
    galera = list()
    galera.append(teste[:])  # copia a lista teste para a lista galera
    print(f'galera => {galera}')
    teste[0] = 'Maria'
    teste[1] = 22
    galera.append(teste[:])  # copia a lista teste para a lista galera
    print(f'galera => {galera}')
    ''')
    teste = list()
    teste.append('Gustavo')
    teste.append(40)
    galera = list()
    galera.append(teste[:])  # copia a lista teste para a lista galera
    print(f'galera => {galera}')
    print('\t\t\t\t0\t\t1\t\t\t\t\t(índices)')
    print('\t\t\t\t\t0\t\t\t\t\t\t(índices)')
    teste[0] = 'Maria'
    teste[1] = 22
    galera.append(teste[:])  # copia a lista teste para a lista galera
    print(f'galera => {galera}')
    print('\t\t\t\t0\t\t1\t\t0\t  1\t\t(índices)')
    print('\t\t\t\t\t0\t\t\t\t1\t\t(índices)')

    cabecalho('Looping para manipular conteúdo da lista', 50, '-')
    print('''\tgalera = list()
    dado = list()
    for c in range(0, 3):
        dado.append(str(input('Nome: ').title().strip()))
        dado.append(int(input('Idade: ').strip()))
        galera.append(dado[:])  # copia a lista dado para a lista galera
        dado.clear()  # apaga o conteúdo da lista dado
        ''')
    galera = list()
    dado = list()
    for c in range(0, 3):
        dado.append(str(input('Nome: ').title().strip()))
        dado.append(int(input('Idade: ').strip()))
        galera.append(dado[:])  # copia a lista dado para a lista galera
        dado.clear()  # apaga o conteúdo da lista dado
    print(f'galera => {galera}')

    print('''
    total_maior = total_menor = 0
    for p in galera:
        if p[1] >= 21:
            print(f'{p[0]} é maior de idade.')
            total_maior += 1
        else:
            print(f'{p[0]} é menor de idade.')
            total_menor += 1
    print(f'\nTemos {total_maior} maior(es) e {total_menor} menor(es).')
    ''')
    total_maior = total_menor = 0
    for p in galera:
        if p[1] >= 21:
            print(f'{p[0]} é maior de idade.')
            total_maior += 1
        else:
            print(f'{p[0]} é menor de idade.')
            total_menor += 1
    print(f'\nTemos {total_maior} maior(es) e {total_menor} menor(es).')
