"""21_ex102_funcao_fatorial.py em 2018-12-24. Projeto Curso em Video.

Função para Fatorial

Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo do fatorial.

"""
from funcoes import cabecalho


def fatorial(n: int, show: bool = False) -> object:
    """-> Calcula fatorial de um número.

    :param n: fatorial de n.
    :type n: int
    :param show: (opcional) mostrar ou não o desenvolvimento do fatorial.
    :type show: bool
    :return: fatorial de um número n.
    :rtype: object
    """
    f = 1
    corpo = ''
    for k in range(n, 0, -1):
        f *= k
        corpo += f'{k}{" x " if k > 1 else " = "}'
    if show:
        return f'{corpo}{f}'
    else:
        return f


if __name__ == '__main__':
    cabecalho('Função para Fatorial')

    print('''\tdef fatorial(n, show=False):
        f = 1
        corpo = ''
        for k in range(n, 0, -1):
            f *= k
            corpo += f'{k}{" x " if k > 1 else " = "}'
        if show:
            return f'{corpo}{f}'
        else:
            return f
    
    print(f'5! = {fatorial(5, True)}')
    print(f'5! = {fatorial(5)}')
    print(f'6! = {fatorial(6, True)}')
    print(f'6! = {fatorial(6)}')
    help(fatorial)
    ''')
    print(f'5! = {fatorial(5, True)}')
    print(f'5! = {fatorial(5)}')
    print(f'6! = {fatorial(6, True)}')
    print(f'6! = {fatorial(6)}')
    help(fatorial)
