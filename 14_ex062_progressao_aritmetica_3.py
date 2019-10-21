"""14_ex062_progressao_aritmetica_3.py em 2018-12-17. Projeto Curso em Video.

Super Progressão Aritmética v3.0

Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.



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
    cabecalho('Super Progressão Aritmética v3.0')

    print('''\tfrom funcoes import cabecalho, verificador
    
    c = 0
    n = 10
    a1 = verificador('1° termo: ')
    r = verificador('Razão da PA: ')
    termo = a1
    while True:
        if c == n:
            mais = verificador('\\nQuantos termos você quer mostrar mais? ')
            n += mais
            if mais == 0:
                break
        c += 1
        print(f'{termo}{" ->" if c < n else " PAUSA"}', end=' ')
        termo += r
    Sn = n / 2 * (a1 + (a1 + (n - 1) * r))
    print(f'Progressão finalizado com {n} termos.\nA soma dos termos é {Sn:.0f}.')
    ''')
    c = 0
    n = 10
    a1 = verificador('1° termo: ')
    r = verificador('Razão da PA: ')
    termo = a1
    while True:
        if c == n:
            mais = verificador('\nQuantos termos você quer mostrar mais? ')
            n += mais
            if mais <= 0:
                break
        c += 1
        print(f'{termo}{" ->" if c < n else " PAUSA"}', end=' ')
        termo += r
    Sn = n / 2 * (a1 + (a1 + (n - 1) * r))
    print(f'Progressão finalizado com {n} termos.\nA soma dos termos é {Sn:.0f}.')
