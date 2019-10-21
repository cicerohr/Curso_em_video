"""20_ex098_funcao_contador.py em 2018-12-23. Projeto Curso em Video.

Função de Contador

Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1;
b) de 10 até 0, de 2 em 2;
c) uma contagem personalizada.

"""
from time import sleep
from funcoes import cabecalho, verificador


def contador(i: int, f: int, p: int):
    """Faz contagem progressiva ou regressiva

    :param i: início
    :type i: int
    :param f: fim
    :type f: int
    :param p: passo
    :type p: int
    """
    if f > 0:
        f += 1
    else:
        f -= 1
        if p > 0:
            p *= -1
    for k in range(i, f, p):
        print(k, flush=True, end=' ')
        sleep(1)


if __name__ == '__main__':
    cabecalho('Função de Contador')

    print('''\t
    ''')
    print('-' * 30, '\n', 'Contagem de 1 a 10 de 1 em 1.', sep='')
    contador(1, 10, 1)
    print('FIM!')
    print('-' * 30, '\n', 'Contagem de 10 a 0 de 2 em 2.', sep='')
    contador(10, 0, -2)
    print('FIM!')
    print('-' * 30, '\n', 'Agora é a sua vez de personalizar a contagem!', sep='')
    inicio = verificador('Início: ')
    fim = verificador('Fim: ')
    passo = verificador('Passo: ')
    print('-' * 30, '\n', f'Contagem de {inicio} a {fim} de {abs(passo)} em {abs(passo)}.', sep='')
    contador(inicio, fim, passo)
    print('FIM!')
