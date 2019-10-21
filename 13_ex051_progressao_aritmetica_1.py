"""13_ex051_progressao_aritmetica_1.py em 2018-12-15. Projeto Curso em Video.

Progressão Aritmética v1.0

Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.


Definição PA
Uma progressão aritmética é uma sequência numérica definida recursivamente por:

aₙ = aₙ₋₁ + r, n > 1,
onde o primeiro termo, a₁, é um número dado. O número r é chamado de razão da progressão aritmética.

Notamos que:

r = aₙ - aₙ₋₁, n > 1.

Fórmula do termo geral
O n-ésimo termo de uma progressão aritmética, denotado por aₙ pode ser obtido por meio da fórmula:

aₙ = a₁ + (n - 1) * r

em que:
a₁ é o primeiro termo;
r é a razão.
Fonte: https://pt.wikipedia.org/wiki/Progressão_aritmética#Definição

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Progressão Aritmética')

    print('''\ta1 = verificador('Primeiro termo: ')
    r = verificador('Razão: ')
    # número de termos
    n = 10
    # O n-ésimo termo de uma progressão aritmética
    an = a1 + (n - 1) * r
    #         range(start, stop[, step])
    for pa in range(a1, an + 1, r):
        print(f'{pa}', end=' -> ')
    print('Acabou')
    ''')
    a1 = verificador('Primeiro termo: ')
    r = verificador('Razão: ')
    # número de termos
    n = 10
    # O n-ésimo termo de uma progressão aritmética
    an = a1 + (n - 1) * r
    #         range(start, stop[, step])
    for pa in range(a1, an + 1, r):
        print(f'{pa}', end=' -> ')
    print('Acabou')
