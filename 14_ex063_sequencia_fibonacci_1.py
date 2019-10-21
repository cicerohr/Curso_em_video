"""14_ex063_sequencia_fibonacci_1.py em 2018-12-17. Projeto Curso em Video.

Sequência de Fibonacci v1.0

Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
           f1 +f2 = f3


Em termos matemáticos, a sequência é definida recursivamente pela fórmula abaixo, sendo o primeiro termo F1 = 1:

F_{n} = F_{n-1} + F_{n-2},

e valores iniciais

F_{1} = 1, F_{2} = 1.
Fonte = https://pt.wikipedia.org/wiki/Sequência_de_Fibonacci

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Sequência de Fibonacci v1.0')

    print('''\tfrom funcoes import cabecalho, verificador
    
    c = 2
    f1 = 0
    f2 = 1
    termos = verificador('Quantos termos você quer mostrar? ')
    print('0 -> 1', end=' -> ')
    while termos > c:
        fn = f1 + f2
        f1 = f2
        f2 = fn
        c += 1
        print(f'{fn}{" -> " if termos > c else " -> FIM"}', end='')
    ''')
    c = 2
    f1 = 0
    f2 = 1
    termos = verificador('Quantos termos você quer mostrar? ')
    print('0 -> 1', end=' -> ')
    while termos > c:
        fn = f1 + f2
        f1 = f2
        f2 = fn
        c += 1
        print(f'{fn}{" -> " if termos > c else " -> FIM"}', end='')
