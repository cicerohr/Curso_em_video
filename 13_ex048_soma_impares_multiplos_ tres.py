"""13_ex048_soma_impares_multiplos_ tres.py em 2018-12-15. Projeto Curso em Video.

Soma ímpares múltiplos de três

Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que
se encontram no intervalo de 1 até 500.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Soma ímpares múltiplos de três')

    print('''\tsoma = conta = 0
    for k in range(1, 501, 2):
        if k % 3 == 0:
            soma += k
            conta += 1
    print(f'\nA soma de todos os {conta} valores solicitados é {soma}.')
    ''')
    soma = conta = 0
    for k in range(1, 501, 2):
        if k % 3 == 0:
            soma += k
            conta += 1
    print(f'\nA soma de todos os {conta} valores solicitados é {soma}.')
