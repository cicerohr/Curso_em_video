"""13_ex050_soma_pares.py em 2018-12-15. Projeto Curso em Video.

Soma dos pares

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Soma dos pares')

    print('''\tfrom funcoes import cabecalho, verificador
    
    soma = conta = 0
    for k in range(1, 7):
        numero = verificador(f'Digite {k}° número: ')
        if numero % 2 == 0 and numero != 0:
            soma += numero
            conta += 1
    if conta == 0:
        print(f'\\nVocê não digitou números pares.')
    elif conta == 1:
        print(f'\\nFoi digitado apenas um número par que é {soma}.')
    else:
        print(f'\\nA soma dos {conta} números pares foi {soma}.')
    ''')
    soma = conta = 0
    for k in range(1, 7):
        numero = verificador(f'Digite {k}° número: ')
        if numero % 2 == 0 and numero != 0:
            soma += numero
            conta += 1
    if conta == 0:
        print(f'\nVocê não digitou números pares.')
    elif conta == 1:
        print(f'\nFoi digitado apenas um número par que é {soma}.')
    else:
        print(f'\nA soma dos {conta} números pares foi {soma}.')

