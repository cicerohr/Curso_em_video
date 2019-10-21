"""07_ex009_tabuada_1.py em 2018-12-10. Projeto Curso em Video.

Tabuada V.1.0

Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Tabuada V.1.0')

    print('''\tn = int(input('Digite um número inteiro para ver sua tabuada: '))
    print('-' * 12)
    for t in range(0, 11):
        print(f'{n} x {t:2} = {n * t}')
    print('-' * 12)
    ''')
    n = verificador('Digite um número inteiro para ver sua tabuada: ')
    print('-' * 12)
    for t in range(0, 11):
        print(f'{n} x {t:2} = {n * t}')
    print('-' * 12)
    help(verificador)
