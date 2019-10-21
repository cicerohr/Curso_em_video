"""09_ex023_separando_digitos_n.py em 2018-12-11. Projeto Curso em Video.

Separando dígitos de um número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Separando dígitos de um número')

    print('''\tn = verificador('Digite um número: ')
    print(f'Analisando o número {n}.')
    u = n // 1 % 10         Ex.: 1234 // 1 => 1234 % 10 => 4
    d = n // 10 % 10        Ex.: 1234 // 10 => 123 % 10 => 3
    c = n // 100 % 10       Ex.: 1234 // 100 => 12 % 10 => 2
    m = n // 1000 % 10      Ex.: 1234 // 1000 => 1 % 10 => 1
    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'Centena: {c}')
    print(f'Milhar: {m}')
    ''')
    n = verificador('Digite um número: ')
    print(f'Analisando o número {n}.')
    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10
    m = n // 1000 % 10
    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'Centena: {c}')
    print(f'Milhar: {m}')
