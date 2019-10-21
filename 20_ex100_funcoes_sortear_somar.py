"""20_ex100_funcoes_sortear_somar.py em 2018-12-24. Projeto Curso em Video.

Funções para sortear e somar

Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

"""
from random import sample
from time import sleep
from funcoes import cabecalho


def sorteia(q_n=1):
    """Sorteia n números entre 0 e 99 e coloca em uma lista

    :param q_n: Quantidade de número a ser sorteados
    :type q_n: int
    :return: lista com n números sorteados
    :rtype: list
    """
    return sample([k for k in range(100)], q_n)


def soma_par(lista):
    """Soma todos os pares de uma lista

    :param lista: população
    :type lista: list
    :return: soma de pares da lista
    :rtype: int
    """
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    return soma


if __name__ == '__main__':
    cabecalho('Funções para sortear e somar')

    print('''\tfrom random import sample
    from time import sleep
    
    
    def sorteia():
        return sample([k for k in range(100)], 5)


    def soma_par(lista):
        soma = 0
        for v in lista:
            if v % 2 == 0:
                soma += v
        return soma
    
    
    numeros = sorteia()
    print(f'Sorteando {len(numeros)} valores da lista:', end=' ')
    for n in numeros:
        print(n, end=' ')
        sleep(0.3)
    print('Pronto!')
    print(f'Somando os valores pares de {numeros}, temos {soma_par(numeros)}.')
    ''')
    numeros = sorteia(5)
    print(f'Sorteando {len(numeros)} valores da lista:', end=' ')
    for n in numeros:
        print(n, end=' ')
        sleep(0.3)
    print('Pronto!')
    print(f'Somando os valores pares de {numeros}, temos {soma_par(numeros)}.')
