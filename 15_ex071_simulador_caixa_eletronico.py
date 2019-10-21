"""15_ex071_simulador_caixa_eletronico.py em 2018-12-18. Projeto Curso em Video.

Simulador de Caixa Eletrônico

Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

"""
from funcoes import cabecalho, verificador, ansi

if __name__ == '__main__':
    cabecalho('Simulador de Caixa Eletrônico')

    print('''\tfrom funcoes import cabecalho, verificador, ansi
    
    cedulas = (100, 50, 20, 10, 5, 1)
    c = 0
    print('=' * 44, f'\\n{ansi("bold", "azul")}', 'Banco CEV'.center(44).upper(), f'{ansi()}\\n', '=' * 44, sep='')
    saque = verificador('Qual o valor que você quer sacar? R$ ')
    while saque != 0:
        n_cedulas = saque // cedulas[c]
        if n_cedulas != 0:
            print(f'Total de {n_cedulas} cédula{"s" if n_cedulas > 1 else ""} de R$ {cedulas[c]:.2f}.')
        saque = saque % cedulas[c]
        c += 1
    print('=' * 44, '\\n', 'Volte sempre ao banco CEV. Tenha um bom dia!', sep='')
    ''')
    cedulas = (100, 50, 20, 10, 5, 1)
    c = 0
    print('=' * 44, f'\n{ansi("bold", "azul")}', 'Banco CEV'.center(44).upper(), f'{ansi()}\n', '=' * 44, sep='')
    saque = verificador('Qual o valor que você quer sacar? R$ ')
    while saque != 0:
        n_cedulas = saque // cedulas[c]
        if n_cedulas != 0:
            print(f'Total de {n_cedulas} cédula{"s" if n_cedulas > 1 else ""} de R$ {cedulas[c]:.2f}.')
        saque = saque % cedulas[c]
        c += 1
    print('=' * 44, '\n', 'Volte sempre ao banco CEV. Tenha um bom dia!', sep='')
