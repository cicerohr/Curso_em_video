"""18_ex086_matriz.py em 2018-12-20. Projeto Curso em Video.

Matriz em Python

Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Matriz em Python')

    print('''\tfrom funcoes import cabecalho, verificador
    
    matriz = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for x in range(3):
        for y in range(3):
            matriz[x][y] = verificador(f'Digite um valor para [{x}, {y}]: ')
    print('-=' * 30)
    for l in range(3):
        for c in range(3):
            print(f'[{str(matriz[l][c]).center(5)}]', end='')
        print()
    ''')
    matriz = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for x in range(3):
        for y in range(3):
            matriz[x][y] = verificador(f'Digite um valor para [{x}, {y}]: ')
    print('-=' * 30)
    for l in range(3):
        for c in range(3):
            print(f'[{str(matriz[l][c]).center(5)}]', end='')
        print()
