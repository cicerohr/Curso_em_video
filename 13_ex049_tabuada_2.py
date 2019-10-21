"""13_ex049_tabuada_2.py em 2018-12-15. Projeto Curso em Video.

Tabuada v.2.0

Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Tabuada v.2.0')

    print('''\tnumero = so_numero('Digite um número pra ver sua tabuada: ')
    for k in range(1, 11):
        print(f'{numero} x {k:2} = {numero * k}')
    ''')
    numero = verificador('Digite um número pra ver sua tabuada: ')
    for k in range(1, 11):
        print(f'{numero} x {k:2} = {numero * k}')
