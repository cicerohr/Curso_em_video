"""14_ex061_progressao_aritmetica_2.py em 2018-12-16. Projeto Curso em Video.

Progressão Aritmética v2.0

Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.


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

Soma dos termos de uma progressão aritmética
Sn = n/2 * (a1 + an)
Fonte: https://pt.wikipedia.org/wiki/Progressão_aritmética#Definição

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Progressão Aritmética v2.0')

    print('''\tfrom funcoes import cabecalho, verificador
    
    c = 0
    n = 10
    a1 = verificador('1° termo: ')
    r = verificador('Razão da PA: ')
    an = a1 + (n - 1) * r
    Sn = n / 2 * (a1 + an)
    while c < n:
        c += 1
        print(f'{a1}{" ->" if c < n else " ="}', end=' ')
        a1 += r
    print(f'{Sn:.0f}')
    ''')
    c = 0
    n = 10
    a1 = verificador('1° termo: ')
    r = verificador('Razão da PA: ')
    an = a1 + (n - 1) * r
    Sn = n / 2 * (a1 + an)
    while c < n:
        c += 1
        print(f'{a1}{" ->" if c < n else " ="}', end=' ')
        a1 += r
    print(f'{Sn:.0f}')
