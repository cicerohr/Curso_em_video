"""15______interrompendo_repeticoes_while.py em 2018-12-07. Projeto Curso em Video.

Interrompendo repetições while

Nessa aula, vamos aprender como utilizar a instrução break e os looping infinitos a favor das nossas estratégias
de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um
laço no meio do destino.
Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

"""
from funcoes import cabecalho

if __name__ == '__main__':
    cabecalho('Interrompendo repetições while')

    print('''\tn = s = 0
    while True:
        n = int(input('Digite um número? '))
        if n == 999:
            print(f'A soma vale {s}.')
            break
        s += n
        ''')
    n = s = 0
    while True:
        n = int(input('Digite um número? '))
        if n == 999:
            print(f'A soma vale {s}.')  # Python 3.6+ (fstrings)
            print('A soma vale {}.'.format(s))  # Python 3
            print('A soma vale %d.' % s)  # Python 2
            break
        s += n
