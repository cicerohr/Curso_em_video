"""18_ex087_mais_matriz.py em 2018-12-20. Projeto Curso em Video.

Mais sobre Matriz em Python

Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

"""
from funcoes import cabecalho, verificador

if __name__ == '__main__':
    cabecalho('Mais sobre Matriz em Python')

    print('''\tfrom funcoes import cabecalho, verificador
    
    pares = tc = 0
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(3):
        for y in range(3):
            matriz[x][y] = verificador(f'Digite um valor para [{x}, {y}]: ')
    print('-=' * 15)
    for l in range(3):
        for c in range(3):
            print(f'[{str(matriz[l][c]).center(5)}]', end='')
            if matriz[l][c] % 2 == 0:
                pares += matriz[l][c]
            if c == 2:
                tc += matriz[l][2]
        print()
    print('-=' * 15, '\\n', f'A soma dos valores pares é {pares}.', sep='')
    print(f'A soma dos valores da terceira coluna é {tc}.')
    print(f'O maior valor da segunda linha é {max(matriz[1])}')
    ''')
    pares = tc = 0
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(3):
        for y in range(3):
            matriz[x][y] = verificador(f'Digite um valor para [{x}, {y}]: ')
    print('-=' * 15)
    for l in range(3):
        for c in range(3):
            print(f'[{str(matriz[l][c]).center(5)}]', end='')
            if matriz[l][c] % 2 == 0:
                pares += matriz[l][c]
            if c == 2:
                tc += matriz[l][2]
        print()
    print('-=' * 15, '\n', f'A soma dos valores pares é {pares}.', sep='')
    print(f'A soma dos valores da terceira coluna é {tc}.')
    print(f'O maior valor da segunda linha é {max(matriz[1])}')
