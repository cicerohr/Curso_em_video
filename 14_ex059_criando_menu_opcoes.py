"""14_ex059_criando_menu_opcoes.py em 2018-12-16. Projeto Curso em Video.

Criando um Menu de Opções

Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

"""
from time import sleep
from funcoes import cabecalho, verificador, ansi

if __name__ == '__main__':
    cabecalho('Criando um Menu de Opções')

    print('''\tfrom time import sleep
    from funcoes import cabecalho, verificador, ansi
    
    menu = {1: 'somar', 2: 'multiplicar', 3: 'maior', 4: 'novos números', 5: 'sair do programa'}
    valor_1 = verificador('1° valor: ')
    valor_2 = verificador('2° valor: ')
    while True:
        for k, v in menu.items():
            print(f'\\t[{k}] {v}')
        opcao = verificador(f'\\n{">" * 5} Qual sua opção? ')
        if 1 <= opcao <= 5:
            if opcao == 1:
                print(f'A soma entre {valor_1} e {valor_2} é {valor_1 + valor_2}.')
            elif opcao == 2:
                print(f'O resultado de {valor_1} x {valor_2} é {valor_1 * valor_2}.')
            elif opcao == 3:
                print(f'Entre {valor_1} e {valor_2} o maior valor é {max(valor_1, valor_2)}.')
            elif opcao == 4:
                print('Informe os números novamente:')
                valor_1 = verificador('1° valor: ')
                valor_2 = verificador('2° valor: ')
            else:
                print('FINALIZANDO...', flush=True)
                sleep(1)
                break
        else:
            print(f'\\n{ansi("vermelho")}Digite um número entre 1 e 5. Tente novamente!{ansi()}\\n')
        print('=-=' * 9)
    ''')
    menu = {1: 'somar', 2: 'multiplicar', 3: 'maior', 4: 'novos números', 5: 'sair do programa'}
    valor_1 = verificador('1° valor: ')
    valor_2 = verificador('2° valor: ')
    while True:
        for k, v in menu.items():
            print(f'\t[{k}] {v}')
        opcao = verificador(f'\n{">" * 5} Qual sua opção? ')
        if 1 <= opcao <= 5:
            if opcao == 1:
                print(f'A soma entre {valor_1} e {valor_2} é {valor_1 + valor_2}.')
            elif opcao == 2:
                print(f'O resultado de {valor_1} x {valor_2} é {valor_1 * valor_2}.')
            elif opcao == 3:
                print(f'Entre {valor_1} e {valor_2} o maior valor é {max(valor_1, valor_2)}.')
            elif opcao == 4:
                print('Informe os números novamente:')
                valor_1 = verificador('1° valor: ')
                valor_2 = verificador('2° valor: ')
            else:
                print('FINALIZANDO...', flush=True)
                sleep(1)
                break
        else:
            print(f'\n{ansi("vermelho")}Digite um número entre 1 e 5. Tente novamente!{ansi()}\n')
        print('=-=' * 9)
