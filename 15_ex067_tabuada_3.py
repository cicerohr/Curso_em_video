"""15_ex067_tabuada_3.py em 2018-12-17. Projeto Curso em Video.

Tabuada v3.0

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Tabuada v3.0')

    print('''\tfrom funcoes import cabecalho, verificador
    
    while True:
        v = verificador('Quer ver tabuada de qual a valor? ')
        print('-' * 35)
        if v < 0:
            print('Programa de tabuada encerrado. Volte sempre!')
            break
        for k in range(1, 11):
            print(f'{v} x {k:2} = {v * k}')
        print('-' * 35)
    ''')
    while True:
        v = verificador('Quer ver tabuada de qual a valor? ')
        print('-' * 35)
        if v < 0:
            print('Programa de tabuada encerrado. Volte sempre!')
            break
        for k in range(1, 11):
            print(f'{v} x {k:2} = {v * k}')
        print('-' * 35)
