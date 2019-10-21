"""20_ex099_funcao_descobre_maior.py em 2018-12-24. Projeto Curso em Video.

Função que descobre o maior

Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

"""
from funcoes import cabecalho


def maior(*args):
    """Verifica o maior em uma sequência de números

    :param args: vários argumentos
    :type args: object
    """
    print('-' * 40, '\n', 'Analisando os valores passados...', sep='')
    print(f'{args} Foram informados {len(args)} valores ao todo.')
    print(f'O maior valor informado foi {max(args) if args else 0}.')


if __name__ == '__main__':
    cabecalho('Função que descobre o maior')

    print('''\tdef maior(*args):
        print('-' * 40, '\\n', 'Analisando os valores passados...', sep='')
        print(f'{args} Foram informados {len(args)} valores ao todo.')
        print(f'O maior valor informado foi {max(args) if args else 0}.')
    
    maior(2, 9, 4, 7, 5, 1)
    maior(4, 7, 0)
    maior(1, 2)
    maior(6)
    maior()
    ''')
    maior(2, 9, 4, 7, 5, 1)
    maior(4, 7, 0)
    maior(1, 2)
    maior(6)
    maior()
