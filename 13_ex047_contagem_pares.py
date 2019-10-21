"""13_ex047_contagem_pares.py em 2018-12-15. Projeto Curso em Video.

Contagem de pares

Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Contagem de pares')

    print("""\tfor k in range(2, 51, 2):
        print(k, end=' ')
    print('Acabou!')
    """)
    for k in range(2, 51, 2):
        print(k, end=' ')
    print('Acabou!')
