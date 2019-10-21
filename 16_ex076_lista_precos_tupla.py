"""16_ex076_lista_precos_tupla.py em 2018-12-19. Projeto Curso em Video.

Lista de Preços com Tupla

Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Lista de Preços com Tupla')

    print('''\tprecos = ('Lápis', 1.75,
              'Borracha', 2,
              'Caderno', 15.90,
              'Estojo', 25,
              'Transferidor', 4.2,
              'Compasso', 9.99,
              'Mochila', 120.32,
              'Canetas', 22.3,
              'Livro', 34.9)
    print('-' * 40, '\\n', 'Listagem de Preços'.center(40).upper(), '\\n', '-' * 40, sep='')
    for k, v in enumerate(precos):
        if k % 2 == 0:
            print(f'{v}'.ljust(31, '.'), end='')
        else:
            print('R$', f'{v:.2f}'.rjust(6))
    print('-' * 40)
    ''')
    precos = ('Lápis', 1.75,
              'Borracha', 2,
              'Caderno', 15.90,
              'Estojo', 25,
              'Transferidor', 4.2,
              'Compasso', 9.99,
              'Mochila', 120.32,
              'Canetas', 22.3,
              'Livro', 34.9)
    print('-' * 40, '\n', 'Listagem de Preços'.center(40).upper(), '\n', '-' * 40, sep='')
    for k, v in enumerate(precos):
        if k % 2 == 0:
            print(f'{v}'.ljust(31, '.'), end='')
        else:
            print('R$', f'{v:.2f}'.rjust(6))
    print('-' * 40)
