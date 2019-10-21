"""12_ex037_conversor_bases_numericas.py em 2018-12-14. Projeto Curso em Video.

Conversor de Bases Numéricas

Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

"""
from funcoes import cabecalho, ansi, verificador

if __name__ == '__main__':
    cabecalho('Conversor de Bases Numéricas')

    print('''\tfrom cicero import cabecalho, verificador, ansi
    
    menu = {1: 'BINÁRIO', 2: 'OCTAL', 3: 'HEXADECIMAL'}
    numero = verificador('Digite um número inteiro: ')
    while True:
        print('\nEscolha uma das bases de conversão:')
        for k, v in menu.items():
            print(f'[{k}] converte para {v}')
        opcao = verificador('\nSua opção: ')
        if 1 <= opcao <= 3:
            print(f'\n{numero} convertido para {menu[opcao]} é igual a{ansi("bold", "cyan")}', end=' ')
            if opcao == 1:
                print(bin(numero)[2:])
                break
            elif opcao == 2:
                print(oct(numero)[2:])
                break
            elif opcao == 3:
                print(hex(numero)[2:])
                break
        else:
            print(f'\n{ansi("bold", "vermelho")}Digite um número entre 1 e 3! Tente novamente!{ansi()}')
    ''')
    menu = {1: 'BINÁRIO', 2: 'OCTAL', 3: 'HEXADECIMAL'}
    numero = verificador('Digite um número inteiro: ')
    while True:
        print('\nEscolha uma das bases de conversão:')
        for k, v in menu.items():
            print(f'[{k}] converte para {v}')
        opcao = verificador('\nSua opção: ')
        if 1 <= opcao <= 3:
            print(f'\n{numero} convertido para {menu[opcao]} é igual a{ansi("bold", "cyan")}', end=' ')
            if opcao == 1:
                print(bin(numero)[2:])
                break
            elif opcao == 2:
                print(oct(numero)[2:])
                break
            elif opcao == 3:
                print(hex(numero)[2:])
                break
        else:
            print(f'\n{ansi("bold", "vermelho")}Digite um número entre 1 e 3! Tente novamente!{ansi()}')
