"""13_ex052_numeros_primos.py em 2018-12-16. Projeto Curso em Video.

Números primos

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""
from funcoes import cabecalho, verificador, ansi

if __name__ == '__main__':
    cabecalho('Números primos')

    print('''\tfrom cicero import cabecalho, verificador, ansi
    
    conta = 0
    n = verificador('Digite um número: ')
    for k in range(1, n + 1):
        if n % k == 0:
            print(f'{ansi("amarelo")}{k}{ansi()}', end=' ')
            conta += 1
        else:
            print(f'{ansi("vermelho")}{k}{ansi()}', end=' ')
    print(f'\\nO número {n} foi divisível {conta} vezes.')
    if conta <= 2:
        print('Portanto é primo!')
        pass
    else:
        print('Portanto não é primo!')
    ''')
    conta = 0
    n = verificador('Digite um número: ')
    for k in range(1, n + 1):
        if n % k == 0:
            print(f'{ansi("amarelo")}{k}{ansi()}', end=' ')
            conta += 1
        else:
            print(f'{ansi("vermelho")}{k}{ansi()}', end=' ')
    print(f'\nO número {n} foi divisível {conta} vezes.')
    if conta == 2:
        print('Portanto é primo!')
        pass
    else:
        print('Portanto não é primo!')
